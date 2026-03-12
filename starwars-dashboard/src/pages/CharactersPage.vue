<template>
  <q-page padding>

    <q-btn
      label="Novo Personagem"
      color="primary"
      @click="openForm"
    />

    <q-table
      title="Personagens Star Wars"
      :rows="characters"
      :columns="columns"
      row-key="id"
    >

      <template v-slot:body-cell-actions="props">
        <q-btn
          color="primary"
          icon="edit"
          flat
          @click="editCharacter(props.row)"
        />

        <q-btn
          color="negative"
          icon="delete"
          flat
          @click="deleteCharacter(props.row.id)"
        />
      </template>

    </q-table>

  </q-page>
</template>

<script>
import api from 'src/services/api';

export default {
	data() {
		return {
			characters: [],
			columns: [
				{ name: "name", label: "Nome", field: "name" },
        { name: "height", label: "Altura", field: "height" },
        { name: "mass", label: "Peso", field: "mass" },
        { name: "gender", label: "Gênero", field: "gender" },
        { name: "actions", label: "Ações", field: "actions" }
			]
		}
	},

	mounted(){
		this.getCharacters()
	},

	methods: {

		async getCharacters() {
			const response = await api.get("/characters/")
			this.characters = response.data
		},

		async deleteCharacter(id) {
			await api.delete(`/characters/${id}/`)
			this.getCharacters()
		}
	}
}
</script>