<template>
  <v-card class="mx-auto">
    <v-row>
      <v-col v-for="(item, i) in candidates" :key="i" cols="10" style="margin: 2%">
        <v-card :color="white" light>
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="headline" v-text="item.name"></v-card-title>
              <v-card-subtitle style="color:black">Votes: {{ item.votes }}</v-card-subtitle>
              <v-card-subtitle>
                <v-expansion-panels v-model="panel" :disabled="disabled">
                  <v-expansion-panel>
                    <v-expansion-panel-header>Details</v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <b>Number of Challenges Solved:</b> {{ item.no_challenges_solved }}
                      <br />
                      <b>Python Rating:</b> {{ item.python_rating }}
                      <br />
                      <b>DSA Rating:</b> {{ item.dsa_rating }}
                      <br />
                      <b>Java Rating:</b> {{ item.java_rating }}
                      <br />
                      <b>C++ Rating:</b> {{ item.cplus_rating }}
                      <br />
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>
              </v-card-subtitle>
              <v-card-actions>
                <v-btn class="btn-success" style="color:white" text v-on:click="vote(item)">Vote</v-btn>
              </v-card-actions>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-card>
</template>

<!--<template>
    <div class="pt-5">
        <div v-if="candidates && candidates.length">
            <div class="card mb-3" v-for="candidate of candidates" v-bind:key="candidate.id">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <svg class="bd-placeholder-img" width="200" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>{{ candidate.name }}</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">{{ candidate.name.charAt(0) }}</text></svg>
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h5 class="card-title">{{ candidate.name }}</h5>
                            <p class="card-text">Votes: {{ candidate.votes }}</p>
                            <router-link :to="{name: 'edit', params: { id: candidate.id }}" class="btn btn-sm btn-primary">Edit</router-link>
                            <button class="btn btn-danger btn-sm ml-1" v-on:click="vote(candidate)">Vote</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <p  v-if="candidates.length == 0">No candidates</p>
    </div>
</template>-->
<script>
import axios from "axios";
export default {
  data() {
    return {
      candidates: [],
    };
  },
  created() {
    console.log("Here");
    this.all();
  },
  methods: {
    vote: function (candidate) {
      if (confirm("Vote " + candidate.name)) {
        axios
          .post(`http://localhost:8000/api/vote/`, {
            candidate_name: candidate.name,
          })
          .then((response) => {
            console.log(response);
            alert("Voted for" + candidate.name)
            this.all()
          })
          .catch(function (error) {
            if (error.response) {
              console.log(error);
              alert("You are not allowed to vote once");
            }
          });
      }
    },
    all: function () {
      console.log("Getting data");
      axios.get("http://localhost:8000/api/candidate/", {
        auth: {
          username: "admin",
          password: "hello@1234"
        }
      }).then((response) => {
        this.candidates = response.data;
        console.log(response);
      });
    },
  },
};
</script>
