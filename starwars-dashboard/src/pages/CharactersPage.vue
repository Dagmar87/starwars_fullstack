<template>
  <q-page padding>
    <q-btn label="Novo Personagem" color="primary" @click="openForm" />

    <q-table
      title="Personagens Star Wars"
      :rows="characters"
      :columns="columns"
      row-key="id"
      class="q-mt-md"
    >
      <template v-slot:body-cell-actions="props">
        <q-td :props="props">
          <q-btn color="primary" icon="edit" flat @click="editCharacter(props.row)" />

          <q-btn color="negative" icon="delete" flat @click="deleteCharacter(props.row.id)" />
        </q-td>
      </template>
    </q-table>

    <character-form
      :dialog="showForm"
      :character="selectedCharacter"
      @update:dialog="showForm = $event"
      @updated="onUpdated"
    />
  </q-page>
</template>

<script>
import api from '../services/api'
import CharacterForm from '../components/CharacterForm.vue'

export default {
  components: { 'character-form': CharacterForm },
  data() {
    return {
      characters: [],
      showForm: false,
      selectedCharacter: {},
      columns: [
        { name: 'name', label: 'Nome', field: 'name', align: 'left' },
        { name: 'height', label: 'Altura', field: 'height', align: 'left' },
        { name: 'mass', label: 'Peso', field: 'mass', align: 'left' },
        { name: 'gender', label: 'Gênero', field: 'gender', align: 'left' },
        { name: 'actions', label: 'Ações', field: 'actions', align: 'center' },
      ],
    }
  },

  mounted() {
    this.getCharacters()
  },

  methods: {
    async getCharacters() {
      const response = await api.get('/characters/')
      this.characters = response.data
    },

    async deleteCharacter(id) {
      await api.delete(`/characters/${id}/`)
      this.getCharacters()
    },

    openForm() {
      this.selectedCharacter = {
        name: '',
        height: '',
        mass: '',
        gender: '',
        birth_year: '',
      }
      this.showForm = true
    },

    editCharacter(character) {
      this.selectedCharacter = { ...character }
      this.showForm = true
    },

    onUpdated() {
      this.showForm = false
      this.getCharacters()
    },
  },
}
</script>
