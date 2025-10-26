<template>

    <div class="container">
        <n-space vertical>
            <n-button type="primary" @click="showModal = true">
                Open Admin Login Modal
            </n-button>
        </n-space>

        <n-modal v-model:show="showModal" preset="card" title="Login as admin" :style="{ width: '400px' }"
            :bordered="false" :segmented="{
                content: 'soft',
                footer: 'soft'
            }">
            <n-form ref="formRef" :model="formValue" :rules="rules" label-placement="top"
                require-mark-placement="right-hanging">
                <n-form-item label="Email" path="email">
                    <n-input v-model:value="formValue.email" placeholder="Enter admin email"
                        @keydown.enter="handleLogin" />
                </n-form-item>

                <n-form-item label="Password" path="password">
                    <n-input v-model:value="formValue.password" type="password" show-password-on="click"
                        placeholder="Enter admin password" @keydown.enter="handleLogin" />
                </n-form-item>

            </n-form>

            <template #footer>
                <n-space justify="end">
                    <n-button @click="showModal = false">
                        Cancel
                    </n-button>
                    <n-button type="primary" :loading="loading" @click="handleLogin">
                        Login
                    </n-button>
                </n-space>
            </template>
        </n-modal>

    </div>

</template>

<script setup>
import { ref } from 'vue'
import { useMessage } from 'naive-ui'

const adminMail = import.meta.env.VITE_CLIENT_ADMIN_MAIL
const adminPassword = import.meta.env.VITE_CLIENT_ADMIN_PASSWORD

const message = useMessage()
const showModal = ref(false)
const formRef = ref(null)
const loading = ref(false)

const formValue = ref({
    email: '',
    password: '',
})

const validateEmail = (rule, value) => {
    if (!value) {
        return new Error('Email is required')
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!emailRegex.test(value)) {
        return new Error('Please enter a valid email address')
    }

    return true
}

// Password validation function
const validatePassword = (rule, value) => {
    if (!value) {
        return new Error('Password is required')
    }

    if (value.length < 6) {
        return new Error('Password must be at least 6 characters')
    }

    return true
}

const rules = {
    email: [
        {
            required: true,
            validator: validateEmail,
            trigger: ['blur', 'input']
        }
    ],
    password: [
        {
            required: true,
            validator: validatePassword,
            trigger: ['blur', 'input']
        }
    ]
}

const isAdminEmail = formEmail => formEmail === adminMail
const isAdminPassword = formPassword => formPassword == adminPassword
const isAdmin = (formEmail, formPassword) => isAdminEmail(formEmail) && isAdminPassword(formPassword)

const handleLogin = async () => {
    try {
        await formRef.value?.validate()

        loading.value = true

        // API CALL simulation
        await new Promise(resolve => setTimeout(resolve, 1500))

        const mockLogin = (email, password) => {
            return {
                success: isAdmin(email, password)
            }
        }

        const response = mockLogin(formValue.value.email, formValue.value.password)

        if (response.success) {
            message.success('Login successful! Welcome back.')
            sessionStorage.setItem('isAdmin', true)
            showModal.value = false
            formValue.value = {
                email: '',
                password: '',
            }
        } else {
            message.error('Login failed. Please check your credentials.')
        }

    } catch (error) {
        if (error?.errors) {
            message.error('Please fix the form errors')
        } else {
            message.error('An error occurred during login')
            console.error('Login error:', error)
        }
    } finally {
        loading.value = false
    }
}
</script>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>