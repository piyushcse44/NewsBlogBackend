from django.db import models

# Create your models here.



class Business(models.Model):
    cover = models.ImageField(upload_to='business_covers/', default='default.jpg')
    title = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    author_name = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    author_img = models.ImageField(upload_to='business_authors/', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    desc_par1 = models.TextField()
    desc_par2 = models.TextField()
    desc_par3 = models.TextField()
    details_title = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    details_quote = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    details_par1 = models.TextField()
    details_par2 = models.TextField()
    details_par3 = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']




class Entertainment(models.Model):
    cover = models.ImageField(upload_to='business_covers/', default='default.jpg')
    title = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    author_name = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    author_img = models.ImageField(upload_to='business_authors/', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    desc_par1 = models.TextField()
    desc_par2 = models.TextField()
    desc_par3 = models.TextField()
    details_title = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    details_quote = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    details_par1 = models.TextField()
    details_par2 = models.TextField()
    details_par3 = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']




class Politics(models.Model):
    cover = models.ImageField(upload_to='business_covers/', default='default.jpg')
    title = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    author_name = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    author_img = models.ImageField(upload_to='business_authors/', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    desc_par1 = models.TextField()
    desc_par2 = models.TextField()
    desc_par3 = models.TextField()
    details_title = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    details_quote = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    details_par1 = models.TextField()
    details_par2 = models.TextField()
    details_par3 = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']




class Economics(models.Model):
    cover = models.ImageField(upload_to='business_covers/', default='default.jpg')
    title = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    author_name = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    author_img = models.ImageField(upload_to='business_authors/', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    desc_par1 = models.TextField()
    desc_par2 = models.TextField()
    desc_par3 = models.TextField()
    details_title = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    details_quote = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    details_par1 = models.TextField()
    details_par2 = models.TextField()
    details_par3 = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']




class Lifestyle(models.Model):
    cover = models.ImageField(upload_to='business_covers/', default='default.jpg')
    title = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    author_name = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    author_img = models.ImageField(upload_to='business_authors/', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    desc_par1 = models.TextField()
    desc_par2 = models.TextField()
    desc_par3 = models.TextField()
    details_title = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    details_quote = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    details_par1 = models.TextField()
    details_par2 = models.TextField()
    details_par3 = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']



class Technoloy(models.Model):
    cover = models.ImageField(upload_to='business_covers/', default='default.jpg')
    title = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    author_name = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    author_img = models.ImageField(upload_to='business_authors/', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    desc_par1 = models.TextField()
    desc_par2 = models.TextField()
    desc_par3 = models.TextField()
    details_title = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    details_quote = models.CharField(max_length=200, null=False, blank=False, default="unknown")
    details_par1 = models.TextField()
    details_par2 = models.TextField()
    details_par3 = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']



class Gallary(models.Model):
        title = models.CharField(max_length=200,null=False,blank=False,default="Unknown")
        Img = models.ImageField(upload_to='business_covers/', default='default.jpg')
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title
        
        class Meta:
            ordering = ['-created_at']




     











    


    


   

