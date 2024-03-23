operation_parameter_map = {
    '/admin/users/{id}/activate.json-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/admin/users/{id}/anonymize.json-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/admin/users/{id}/deactivate.json-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/admin/users/{id}.json-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'delete_posts'
            },
            {
                'name': 'block_email'
            },
            {
                'name': 'block_urls'
            },
            {
                'name': 'block_ip'
            },
        ]
    },
    '/admin/users/list/{flag}.json-GET': {
        'parameters': [
            {
                'name': 'flag'
            },
            {
                'name': 'order'
            },
            {
                'name': 'asc'
            },
            {
                'name': 'page'
            },
            {
                'name': 'show_emails'
            },
            {
                'name': 'stats'
            },
            {
                'name': 'email'
            },
            {
                'name': 'ip'
            },
        ]
    },
    '/admin/users/{id}.json-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/admin/users/{id}/log_out.json-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/user_avatar/{username}/refresh_gravatar.json-POST': {
        'parameters': [
            {
                'name': 'username'
            },
        ]
    },
    '/admin/users/{id}/silence.json-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'silenced_till'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'message'
            },
            {
                'name': 'post_action'
            },
        ]
    },
    '/admin/users/{id}/suspend.json-PUT': {
        'parameters': [
            {
                'name': 'suspend_until'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'id'
            },
            {
                'name': 'message'
            },
            {
                'name': 'post_action'
            },
        ]
    },
    '/admin/backups.json-POST': {
        'parameters': [
            {
                'name': 'with_uploads'
            },
        ]
    },
    '/admin/backups/{filename}-GET': {
        'parameters': [
            {
                'name': 'filename'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/admin/backups.json-GET': {
        'parameters': [
        ]
    },
    '/admin/backups/{filename}-PUT': {
        'parameters': [
            {
                'name': 'filename'
            },
        ]
    },
    '/admin/badges.json-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'badge_type_id'
            },
        ]
    },
    '/admin/badges/{id}.json-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/admin/badges.json-GET': {
        'parameters': [
        ]
    },
    '/user-badges/{username}.json-GET': {
        'parameters': [
            {
                'name': 'username'
            },
        ]
    },
    '/admin/badges/{id}.json-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'badge_type_id'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/categories.json-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'color'
            },
            {
                'name': 'text_color'
            },
            {
                'name': 'parent_category_id'
            },
            {
                'name': 'allow_badges'
            },
            {
                'name': 'slug'
            },
            {
                'name': 'topic_featured_links_allowed'
            },
            {
                'name': 'permissions'
            },
            {
                'name': 'search_priority'
            },
            {
                'name': 'form_template_ids'
            },
        ]
    },
    '/site.json-GET': {
        'parameters': [
        ]
    },
    '/c/{id}/show.json-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/categories.json-GET': {
        'parameters': [
            {
                'name': 'include_subcategories'
            },
        ]
    },
    '/c/{slug}/{id}.json-GET': {
        'parameters': [
            {
                'name': 'slug'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/categories/{id}.json-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'id'
            },
            {
                'name': 'color'
            },
            {
                'name': 'text_color'
            },
            {
                'name': 'parent_category_id'
            },
            {
                'name': 'allow_badges'
            },
            {
                'name': 'slug'
            },
            {
                'name': 'topic_featured_links_allowed'
            },
            {
                'name': 'permissions'
            },
            {
                'name': 'search_priority'
            },
            {
                'name': 'form_template_ids'
            },
        ]
    },
    '/groups/{id}/members.json-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'usernames'
            },
        ]
    },
    '/admin/groups.json-POST': {
        'parameters': [
            {
                'name': 'group'
            },
        ]
    },
    '/admin/groups/{id}.json-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/groups/{id}.json-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/groups.json-GET': {
        'parameters': [
        ]
    },
    '/groups/{id}/members.json-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/groups/{id}/members.json-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'usernames'
            },
        ]
    },
    '/groups/{id}.json-PUT': {
        'parameters': [
            {
                'name': 'group'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/invites.json-POST': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'email'
            },
            {
                'name': 'skip_email'
            },
            {
                'name': 'custom_message'
            },
            {
                'name': 'max_redemptions_allowed'
            },
            {
                'name': 'topic_id'
            },
            {
                'name': 'group_ids'
            },
            {
                'name': 'group_names'
            },
            {
                'name': 'expires_at'
            },
        ]
    },
    '/invites/create-multiple.json-POST': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'email'
            },
            {
                'name': 'skip_email'
            },
            {
                'name': 'custom_message'
            },
            {
                'name': 'max_redemptions_allowed'
            },
            {
                'name': 'topic_id'
            },
            {
                'name': 'group_ids'
            },
            {
                'name': 'group_names'
            },
            {
                'name': 'expires_at'
            },
        ]
    },
    '/t/{id}/invite.json-POST': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'id'
            },
            {
                'name': 'user'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/notifications.json-GET': {
        'parameters': [
        ]
    },
    '/notifications/mark-read.json-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/posts.json-POST': {
        'parameters': [
            {
                'name': 'raw'
            },
            {
                'name': 'title'
            },
            {
                'name': 'topic_id'
            },
            {
                'name': 'category'
            },
            {
                'name': 'target_recipients'
            },
            {
                'name': 'target_usernames'
            },
            {
                'name': 'archetype'
            },
            {
                'name': 'created_at'
            },
            {
                'name': 'reply_to_post_number'
            },
            {
                'name': 'embed_url'
            },
            {
                'name': 'external_id'
            },
        ]
    },
    '/posts/{id}.json-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'force_destroy'
            },
        ]
    },
    '/posts/{id}.json-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/post_actions.json-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'post_action_type_id'
            },
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'flag_topic'
            },
        ]
    },
    '/posts.json-GET': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'before'
            },
        ]
    },
    '/posts/{id}/replies.json-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/posts/{id}/locked.json-PUT': {
        'parameters': [
            {
                'name': 'locked'
            },
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/posts/{id}.json-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'post'
            },
        ]
    },
    '/posts.json-POST': {
        'parameters': [
            {
                'name': 'raw'
            },
            {
                'name': 'title'
            },
            {
                'name': 'topic_id'
            },
            {
                'name': 'category'
            },
            {
                'name': 'target_recipients'
            },
            {
                'name': 'target_usernames'
            },
            {
                'name': 'archetype'
            },
            {
                'name': 'created_at'
            },
            {
                'name': 'reply_to_post_number'
            },
            {
                'name': 'embed_url'
            },
            {
                'name': 'external_id'
            },
        ]
    },
    '/topics/private-messages/{username}.json-GET': {
        'parameters': [
            {
                'name': 'username'
            },
        ]
    },
    '/topics/private-messages-sent/{username}.json-GET': {
        'parameters': [
            {
                'name': 'username'
            },
        ]
    },
    '/search.json-GET': {
        'parameters': [
            {
                'name': 'q'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/site.json-GET': {
        'parameters': [
        ]
    },
    '/tag_groups.json-POST': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/tag_groups/{id}.json-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/tag/{name}.json-GET': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/tag_groups.json-GET': {
        'parameters': [
        ]
    },
    '/tags.json-GET': {
        'parameters': [
        ]
    },
    '/tag_groups/{id}.json-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/posts.json-POST': {
        'parameters': [
            {
                'name': 'raw'
            },
            {
                'name': 'title'
            },
            {
                'name': 'topic_id'
            },
            {
                'name': 'category'
            },
            {
                'name': 'target_recipients'
            },
            {
                'name': 'target_usernames'
            },
            {
                'name': 'archetype'
            },
            {
                'name': 'created_at'
            },
            {
                'name': 'reply_to_post_number'
            },
            {
                'name': 'embed_url'
            },
            {
                'name': 'external_id'
            },
        ]
    },
    '/t/{id}/timer.json-POST': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'id'
            },
            {
                'name': 'time'
            },
            {
                'name': 'status_type'
            },
            {
                'name': 'based_on_last_post'
            },
            {
                'name': 'category_id'
            },
        ]
    },
    '/t/external_id/{external_id}.json-GET': {
        'parameters': [
            {
                'name': 'external_id'
            },
        ]
    },
    '/latest.json-GET': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'order'
            },
            {
                'name': 'ascending'
            },
        ]
    },
    '/t/{id}.json-GET': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/t/{id}/posts.json-GET': {
        'parameters': [
            {
                'name': 'post_ids[]'
            },
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/top.json-GET': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'period'
            },
        ]
    },
    '/t/{id}.json-DELETE': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/t/{id}/invite.json-POST': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'id'
            },
            {
                'name': 'user'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/t/{id}/notifications.json-POST': {
        'parameters': [
            {
                'name': 'notification_level'
            },
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/t/{id}/bookmark.json-PUT': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/t/{id}/status.json-PUT': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'id'
            },
            {
                'name': 'until'
            },
        ]
    },
    '/t/{id}/change-timestamp.json-PUT': {
        'parameters': [
            {
                'name': 'timestamp'
            },
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/t/-/{id}.json-PUT': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'id'
            },
            {
                'name': 'topic'
            },
        ]
    },
    '/uploads/abort-multipart.json-POST': {
        'parameters': [
            {
                'name': 'external_upload_identifier'
            },
        ]
    },
    '/uploads/complete-external-upload.json-POST': {
        'parameters': [
            {
                'name': 'unique_identifier'
            },
            {
                'name': 'for_private_message'
            },
            {
                'name': 'for_site_setting'
            },
            {
                'name': 'pasted'
            },
        ]
    },
    '/uploads/complete-multipart.json-POST': {
        'parameters': [
            {
                'name': 'unique_identifier'
            },
            {
                'name': 'parts'
            },
        ]
    },
    '/uploads/create-multipart.json-POST': {
        'parameters': [
            {
                'name': 'upload_type'
            },
            {
                'name': 'file_name'
            },
            {
                'name': 'file_size'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/uploads.json-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'synchronous'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/uploads/batch-presign-multipart-parts.json-POST': {
        'parameters': [
            {
                'name': 'part_numbers'
            },
            {
                'name': 'unique_identifier'
            },
        ]
    },
    '/uploads/generate-presigned-put.json-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'file_name'
            },
            {
                'name': 'file_size'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/admin/users/{id}/activate.json-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/admin/users/{id}/anonymize.json-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/users/password-reset/{token}.json-PUT': {
        'parameters': [
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/users.json-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'username'
            },
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'active'
            },
            {
                'name': 'approved'
            },
            {
                'name': 'user_fields[1]'
            },
            {
                'name': 'external_ids'
            },
        ]
    },
    '/admin/users/{id}/deactivate.json-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/admin/users/{id}.json-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'delete_posts'
            },
            {
                'name': 'block_email'
            },
            {
                'name': 'block_urls'
            },
            {
                'name': 'block_ip'
            },
        ]
    },
    '/u/{username}/emails.json-GET': {
        'parameters': [
            {
                'name': 'username'
            },
        ]
    },
    '/u/by-external/{provider}/{external_id}.json-GET': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'provider'
            },
            {
                'name': 'external_id'
            },
        ]
    },
    '/admin/users/list/{flag}.json-GET': {
        'parameters': [
            {
                'name': 'flag'
            },
            {
                'name': 'order'
            },
            {
                'name': 'asc'
            },
            {
                'name': 'page'
            },
            {
                'name': 'show_emails'
            },
            {
                'name': 'stats'
            },
            {
                'name': 'email'
            },
            {
                'name': 'ip'
            },
        ]
    },
    '/u/by-external/{external_id}.json-GET': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'external_id'
            },
        ]
    },
    '/admin/users/{id}.json-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/u/{username}.json-GET': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/directory_items.json-GET': {
        'parameters': [
            {
                'name': 'period'
            },
            {
                'name': 'order'
            },
            {
                'name': 'asc'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/user_actions.json-GET': {
        'parameters': [
            {
                'name': 'offset'
            },
            {
                'name': 'username'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/user-badges/{username}.json-GET': {
        'parameters': [
            {
                'name': 'username'
            },
        ]
    },
    '/admin/users/{id}/log_out.json-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/user_avatar/{username}/refresh_gravatar.json-POST': {
        'parameters': [
            {
                'name': 'username'
            },
        ]
    },
    '/session/forgot_password.json-POST': {
        'parameters': [
            {
                'name': 'login'
            },
        ]
    },
    '/admin/users/{id}/silence.json-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'silenced_till'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'message'
            },
            {
                'name': 'post_action'
            },
        ]
    },
    '/admin/users/{id}/suspend.json-PUT': {
        'parameters': [
            {
                'name': 'suspend_until'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'id'
            },
            {
                'name': 'message'
            },
            {
                'name': 'post_action'
            },
        ]
    },
    '/u/{username}/preferences/avatar/pick.json-PUT': {
        'parameters': [
            {
                'name': 'upload_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/u/{username}/preferences/email.json-PUT': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/u/{username}/preferences/username.json-PUT': {
        'parameters': [
            {
                'name': 'new_username'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/u/{username}.json-PUT': {
        'parameters': [
            {
                'name': 'Api-Key'
            },
            {
                'name': 'Api-Username'
            },
            {
                'name': 'username'
            },
            {
                'name': 'name'
            },
            {
                'name': 'external_ids'
            },
        ]
    },
};