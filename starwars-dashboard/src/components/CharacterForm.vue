<template>

  <q-dialog v-model="internalDialog">

    <q-card style="width:400px">

      <q-card-section>
        <div class="text-h6">Personagem</div>
      </q-card-section>

      <q-card-section>

        <q-input v-model="localCharacter.name" label="Nome" />
        <q-input v-model="localCharacter.height" label="Altura" />
        <q-input v-model="localCharacter.mass" label="Peso" />
        <q-input v-model="localCharacter.gender" label="Gênero" />
        <q-input v-model="localCharacter.birth_year" label="Ano nascimento" />

      </q-card-section>

      <q-card-actions align="right">

        <q-btn
          label="Cancelar"
          flat
          v-close-popup
        />

        <q-btn
          label="Salvar"
          color="primary"
          @click="save"
        />

      </q-card-actions>

    </q-card>

  </q-dialog>

</template>

<script>
import api from '../services/api';

export default {

	props: ["dialog", "character"],

  emits: ["update:dialog", "updated"],

  data() {
    return {
      localCharacter: {}
    }
  },

  computed: {
    internalDialog: {
      get() {
        return this.dialog;
      },
      set(val) {
        this.$emit("update:dialog", val);
      }
    }
  },

  watch: {
    character: {
      handler(newVal) {
        this.localCharacter = { ...newVal };
      },
      immediate: true,
      deep: true
    }
  },

	methods: {

		async save() {

			if(this.localCharacter.id) {

				await api.put(`/characters/${this.localCharacter.id}/`, this.localCharacter)

			} else {

				await api.post("/characters/", this.localCharacter)

			}

			this.$emit("updated")
		}
	}
	
}
</script>