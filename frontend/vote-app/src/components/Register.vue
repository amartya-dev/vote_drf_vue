<template>
  <v-container>
    <v-form @submit="create" ref="form" lazy-validation>
      <v-text-field v-model="admin_id" :counter="250" label="Admin Id" required></v-text-field>
      <v-text-field v-model="admin_password" label="Admin Password" type="password" required></v-text-field>
      <v-text-field v-model="candidate.name" :counter="250" label="Name" required></v-text-field>
      <v-text-field
        v-model="candidate.no_challenges_solved"
        label="Number of challenges solved"
        type="number"
      ></v-text-field>
      <v-select
        v-model="candidate.python_rating"
        :items="ratings"
        :rules="[v => !!v || 'Python Rating is required']"
        label="Python Rating"
        required
      ></v-select>
      <v-select
        v-model="candidate.java_rating"
        :items="ratings"
        :rules="[v => !!v || 'Java Rating is required']"
        label="Java Rating"
        required
      ></v-select>
      <v-select
        v-model="candidate.dsa_rating"
        :items="ratings"
        :rules="[v => !!v || 'DSA Rating is required']"
        label="DSA Rating"
        required
      ></v-select>
      <v-select
        v-model="candidate.cplus_rating"
        :items="ratings"
        :rules="[v => !!v || 'C++ Rating is required']"
        label="C++ Rating"
        required
      ></v-select>
      <v-btn color="primary" type="submit">Submit</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      ratings: [1, 2, 3, 4, 5],
      num: 1,
      candidate: {
        name: "",
        no_challenges_solved: 0,
        java_rating: 1,
        cplus_rating: 1,
        dsa_rating: 1,
        python_rating: 1,
      },
      admin_id: "",
      admin_password: "",
      submitted: false,
    };
  },
  methods: {
    create: function () {
      axios
        .post("http://127.0.0.1:8000/api/candidate/", this.candidate, {
          auth: {
            username: this.admin_id,
            password: this.admin_password,
          },
        })
        .then((response) => {
          console.log(response);
          alert("Registered Succesfuly");
          this.$router.push("/");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
