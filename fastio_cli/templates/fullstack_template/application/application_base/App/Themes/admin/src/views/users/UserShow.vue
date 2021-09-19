<template>
    <div>
        <PageHeading title="User Details"/>
        <v-container v-if="user" class="grey lighten-5">
            <v-row no-gutters>
                <v-col cols="12" sm="6" md="4">
                    <label>ID</label>
                </v-col>
                <v-col cols="6" md="8" >
                    {{user.id}}
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
import PageHeading from '@/components/Page/PageHeading.vue'
import axios from 'axios'

export default {
    name: 'UserShow',
    components: {
        PageHeading
    },
    data () {
        return {
            userApi: 'http://localhost:8009/api/admin/users/',
            totalUsers: 0,
            desserts: [],
            user: null,
            loading: true,
            options: {},
            headers: [
                {
                    text: 'ID',
                    align: 'start',
                    sortable: false,
                    value: 'id'
                },
                { text: 'First Name', value: 'first_name' },
                { text: 'Last Name', value: 'last_name' },
                { text: 'Job Title', value: 'job_title' }
            ]
        }
    },
    mounted () {
        this.getDataFromApi()
    },
    methods: {
        getDataFromApi () {
            this.loading = true;

            axios.get(this.userApi)  // return a Promise
                .then((response) => {
                // Resolve Promise
                console.log(response);
                //   user = response.data.data 
                    this.user = {
                        id: 1,
                        first_name: "Quan",
                        last_name: "Vu",
                        phone: "0901111111"
                    }
                this.loading = false
            })
        
        },
    }
}
</script>