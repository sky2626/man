<template>
    <div>
        <h1>YouTube Video Downloader</h1>
        <form @submit.prevent="downloadVideo">
            <div>
                <input v-model="videoUrl" type="text" id="videoUrl" placeholder="Enter YouTube Video URL" required />
            </div>
            <button type="submit" :disabled="loading">Generate Download Link</button>
        </form>

        <div v-if="downloadLink">
            <p>Click the link below to download the video:</p>
            <a :href="downloadLink" download>Generate link</a>
        </div>

        <div v-if="loading">Generating link...</div>

        <div v-if="error" class="error">{{ error }}</div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const videoUrl = ref('')
const downloadLink = ref(null)
const loading = ref(false)
const error = ref(null)

const downloadVideo = async () => {
    loading.value = true
    error.value = null
    downloadLink.value = null

    try {
        const response = await $fetch('http://127.0.0.1:8000/api/download/', {
            method: 'POST',
            body: { url: videoUrl.value },
        })

        if (response.error) {
            throw new Error(response.error)
        }

        downloadLink.value = response.download_url
    } catch (err) {
        error.value = err.message
    } finally {
        loading.value = false
    }
}
</script>

<style scoped>
h1 {
    font-size: 2rem;
}

form {
    margin-bottom: 20px;
}

button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
}

button:disabled {
    background-color: #ccc;
}

.error {
    color: red;
}
</style>


