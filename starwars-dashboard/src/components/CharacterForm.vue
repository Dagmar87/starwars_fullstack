<template>

  <q-dialog v-model="dialog">

    <q-card style="width:400px">

      <q-card-section>
        <div class="text-h6">Personagem</div>
      </q-card-section>

      <q-card-section>

        <q-input v-model="character.name" label="Nome" />
        <q-input v-model="character.height" label="Altura" />
        <q-input v-model="character.mass" label="Peso" />
        <q-input v-model="character.gender" label="Gênero" />
        <q-input v-model="character.birth_year" label="Ano nascimento" />

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
import api from 'src/services/api';

export default {

	props: ["dialog", "character"],

	methods: {

		async save() {

			if(this.character.id) {

				await api.put(`/characters/${this.character.id}/`, this.character)

			} else {

				await api.post("/characters/", this.character)

			}

			this.$emit("updated")
		}
	}
	
}
</script>