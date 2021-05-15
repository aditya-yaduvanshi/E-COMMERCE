from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class LISTING(models.Model):
    picture = models.ForeignKey("PICTURE", on_delete=models.CASCADE, related_name="listpic")
    title = models.CharField(max_length=200)
    price = models.FloatField()
    currentprice = models.ForeignKey("BID", on_delete=models.CASCADE, related_name="highestbid")
    category = models.ForeignKey("CATEGORY", on_delete=models.CASCADE, related_name="listtype")
    description = models.CharField(max_length=1000)
    seller = models.ForeignKey("User", on_delete=models.CASCADE, related_name="lister")
    listtime = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    buyer = models.ForeignKey("User", on_delete=models.CASCADE, related_name="winner")
    closetime = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return f"{self.id} : {self.title} , {self.price} , {self.seller} , {self.status}"

class PICTURE(models.Model):
    picture = models.ImageField(upload_to="auctions", blank=True, null=True)
    picurl = models.URLField(blank=True, null=True)
    listing = models.ForeignKey("LISTING", on_delete=models.CASCADE, related_name="piclisting")

    def __str__(self):
        return f"{self.id} : {self.picture} , {self.picurl} , {self.listing}"

class BID(models.Model):
    bid = models.FloatField()
    message = models.CharField(max_length=200, blank=True, null=True)
    bidder = models.ForeignKey("User", on_delete=models.CASCADE, related_name="biduser")
    listing = models.ForeignKey("LISTING", on_delete=models.CASCADE, related_name="bidlisting")
    bidtime = models.DateTimeField(auto_now_add=True)
    feeduser = models.ForeignKey("User", on_delete=models.CASCADE, related_name="blistowner")
    feedback = models.CharField(max_length=200)
    feedtime = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return f"{self.id} : {self.bid} , {self.listing} , {self.bidder}"

class COMMENT(models.Model):
    topic = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)
    commenter = models.ForeignKey("User", on_delete=models.CASCADE, related_name="commentuser")
    listing = models.ForeignKey("LISTING", on_delete=models.CASCADE, related_name="commentlisting")
    commenttime = models.DateTimeField(auto_now_add=True)
    reply = models.CharField(max_length=1000)
    replier = models.ForeignKey("User", on_delete=models.CASCADE, related_name="clistowner")
    replytime = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return f"{self.id} : {self.topic} , {self.commenter} , {self.listing}"

class WATCHLIST(models.Model):
    listing = models.ForeignKey("LISTING", on_delete=models.CASCADE, related_name="watching")
    watcher = models.ForeignKey("User", on_delete=models.CASCADE, related_name="watchuser")

    def __str__(self):
        return f"{self.id} : {self.listing} , {self.watcher}"

class CATEGORY(models.Model):
    category = models.CharField(max_length=200)
    icon = models.URLField()

    def __str__(self):
        return f"{self.id} : {self.category}"

