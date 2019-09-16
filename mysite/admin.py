from mptt.admin import DraggableMPTTAdmin


class GenreAdmin(DraggableMPTTAdmin):
    mptt_ident_field = 'name'
