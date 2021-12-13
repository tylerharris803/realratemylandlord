from django.urls import path
from .views import indexPageView
from .views import viewReviewsPageView
from .views import editReviewsPageView
from .views import deletePageView
from .views import addReviewsPageView, addLandlordPageView, addPropertyPageView
from .views import updateReviewsPageView, landlordDetailPageView, propertyDetailPageView

urlpatterns = [    
    path("viewreviews/", viewReviewsPageView, name="viewreviews"),
    path("editreviews/<int:editID>/", editReviewsPageView, name="editreviews"),
    path("addlandlord/", addLandlordPageView, name="addlandlord"),
    path("addproperty/", addPropertyPageView, name="addproperty"),
    path("update/", updateReviewsPageView, name="update"),
    path("addreviews/", addReviewsPageView, name="addreviews"),
    path("delete/<int:deleteID>/", deletePageView, name="delete"),
    path("landlorddetail/<int:detailID>/", landlordDetailPageView, name="landlorddetail"),
    path("propertydetail/<int:detailID>/", propertyDetailPageView, name="propertydetail"),
    path("", indexPageView, name="index"),
]