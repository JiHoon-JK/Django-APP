from django.contrib import admin
from photo.models import Album, Photo

# Album, Photo 테이블 간에는 1:N 관계가 성리된다. StackedInline -> 세로로 나열되는 형태 / TabularInline -> 가로로 나열되는 형태
class PhotoInline(admin.StackedInline):
    # 추가로 보여주는 테이블은 Photo 테이블이다.
    model = Photo
    # 이미 존재하는 객체 외에 추가로 입력할 수 있는 Photo 테이블 객체의 수는 2개이다.
    extra = 2

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    #앨범 객체 수정 화면을 보여줄 때, PhotoInline 클래스에서 정의한 사항을 같이 보여준다.
    inlines = (PhotoInline,)
    list_display = ('id', 'name', 'description')

# admin.site.register() 함수를 사용해도 되지만 데코레이터를 사용하면 간단하다.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')