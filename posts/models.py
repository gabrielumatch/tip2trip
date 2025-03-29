from django.db import models
from django.contrib.postgres.fields import ArrayField
from users.models import User
from places.models import Place
from routes.models import Route

class Post(models.Model):
    """Model for user posts in the social feed."""
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    mentioned_users = models.ManyToManyField(User, related_name='mentioned_in_posts', blank=True)
    hashtags = models.TextField(blank=True, default='')
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['author', '-created_at']),
        ]

    def __str__(self):
        return f'{self.author.username} - {self.created_at}'

    def like_count(self):
        return self.likes.count()

    @property
    def hashtag_list(self):
        """Return hashtags as a list."""
        return [tag.strip() for tag in self.hashtags.split(',') if tag.strip()]

    def set_hashtags(self, tags):
        """Set hashtags from a list."""
        self.hashtags = ','.join(tags)

class PostMedia(models.Model):
    """Model for media attachments to posts."""
    MEDIA_TYPES = [
        ('IMAGE', 'Image'),
        ('VIDEO', 'Video'),
    ]

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file = models.FileField(upload_to='post_media/')
    caption = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['post', 'order']
        verbose_name_plural = 'Post media'

    def __str__(self):
        return f"{self.get_media_type_display()} for {self.post}"

class Comment(models.Model):
    """Model for comments on posts."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    mentioned_users = models.ManyToManyField(User, related_name='mentioned_in_comments', blank=True)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.author.username} on {self.post}'

    def like_count(self):
        return self.likes.count()

class Report(models.Model):
    """Model for reporting inappropriate content."""
    REPORT_TYPES = [
        ('SPAM', 'Spam'),
        ('INAPPROPRIATE', 'Inappropriate Content'),
        ('HARASSMENT', 'Harassment'),
        ('MISINFORMATION', 'Misinformation'),
        ('OTHER', 'Other'),
    ]

    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports_made')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reports', null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reports', null=True, blank=True)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pending Review'),
            ('REVIEWED', 'Reviewed'),
            ('RESOLVED', 'Resolved'),
            ('DISMISSED', 'Dismissed'),
        ],
        default='PENDING'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        target = self.post or self.comment
        return f"Report on {target.__class__.__name__} by {self.reporter.username}"
