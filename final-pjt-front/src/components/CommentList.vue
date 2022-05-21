<template>
  <div class="comment-list">
    
    <ul>
      <comment-item 
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.pk">
      </comment-item>        
    </ul>

    <comment-form></comment-form>
  </div>
</template>

<script>
import CommentForm from '@/components/CommentForm.vue'
import CommentItem from '@/components/CommentItem.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: { CommentForm, CommentItem },
  props: { comments: Array },
}
</script>

<style></style>