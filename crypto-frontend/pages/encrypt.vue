<template>
    <div id="pageDashboard">
        <v-container grid-list-xl fluid>
            <v-layout column wrap>
                <h1 class="mx-auto">Encrypt</h1>
                <v-card class="mx-auto my-3 py-2 px-4" width="90%">
                    <div class="text-xs-center">
                        <h3>Input</h3>
                    </div>
                    <v-textarea v-model="message" auto-grow  />
                    <div class="text-xs-center">
                        <v-btn v-on:click="sign_message" primary>
                            Encrypt
                        </v-btn>
                    </div>
                </v-card>

                <v-card class="mx-auto my-3 py-2 px-4" width="90%">
                    <div class="text-xs-center">
                        <h3>Output</h3>
                    </div>
                    <div class="output-region">
                        {{output}}
                    </div>
                </v-card>
            </v-layout>
        </v-container>
    </div>
</template>
  
<script>
export default {
    layout: 'dashboard',
    methods: {
        async sign_message() {
            console.log(this.message);
            const data = await this.$http.$post('/api2/encrypt', JSON.parse(this.message));
            console.log(data);
            this.output = JSON.stringify(data, null, 2);;
            console.log(this.output);
        }
    },
    data() {
        return {
            message: "",
            output: {}
        }
    },
}
</script>
<style scoped lang="css">
.output-region {
    min-height: 300px;
    background-color: #eee;
    white-space: pre-line;
    word-break: break-word;
    padding: 20px;
}

* {
    white-space: pre-line;
    word-break: break-word;
}
</style>
  