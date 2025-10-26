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
import PersonInfoTab from './PersonInfoTab.vue';
import PersonReviewsTab from './PersonReviewsTab.vue';
import PersonRolesTab from './PersonRolesTab.vue';

const TITLE = 'Common Person state'

const TABS = [
    { name: 'info', label: 'Info', component: PersonInfoTab },
    { name: 'roles', label: 'Roles', component: PersonRolesTab },
    { name: 'reviews', label: 'Reviews', component: PersonReviewsTab },
]

</script> 