<template>
    <n-spin :show="loading" size="large">
        <n-table :single-line="false">
            <thead>
                <tr>
                    <th v-for="col in COLUMNS" :key="col">{{ col }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(row, rowIndex) in data" :key="rowIndex">
                    <td v-for="col in COLUMNS" :key="col">
                        {{ row[col.toLowerCase()] ?? '...' }}
                    </td>
                </tr>
            </tbody>
        </n-table>
    </n-spin>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useMessage } from 'naive-ui'

const data = ref([])
const loading = ref(false)
const message = useMessage()

const COLUMNS = ['Username', 'Name', 'Email', 'Bio', 'Company', 'Job']

onMounted(async () => {
    loading.value = true
    try {
        const response = await fetch('http://localhost/api/v1/persons?depth=0')
        const result = await response.json()

        data.value = result.map((item) => ({
            username: item.user.username,
            name: item.user.first_name + ' ' + item.user.last_name,
            email: item.user.email,
            bio: item.bio,
            company: item.company,
            job: item.job_title,
        }))
    } catch (err) {
        message.error('Failed to fetch data.')
        console.error(err)
    } finally {
        loading.value = false
    }
})

</script>