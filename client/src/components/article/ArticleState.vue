<template>
    <n-card :title="TITLE" style="margin-bottom: 16px">
        <n-tabs type="line" animated>
            <n-tab-pane v-for="tab in TABS" :key="tab.name" :name="tab.name" :tab="tab.label">
                <component :is="tab.component" />
            </n-tab-pane>
        </n-tabs>
    </n-card>
</template>

<script setup>
import ArticleInfoTab from './ArticleInfoTab.vue';
import ArticleReviewTab from './ArticleReviewTab.vue';
import ArticleRatingTab from './ArticleRatingTab.vue';

const TITLE = 'Common article state'

const TABS = [
    { name: 'info', label: 'Info', component: ArticleInfoTab },
    { name: 'rating', label: 'Rating', component: ArticleRatingTab },
    { name: 'review', label: 'Review', component: ArticleReviewTab },
]

</script>