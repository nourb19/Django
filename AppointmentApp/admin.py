
from django.contrib import admin
from .models import Appointment


class AppointmentAdminPers(admin.ModelAdmin):

    fieldsets = (
        ('Description', {
            'fields': ('reason', 'status', 'prescription')
        }),
        ('Date + Duration', {
            'fields': ('appointment_date', 'duration_minutes')
        }),
        ('Patients/Doctors', {
            'fields': ('doctor', 'patient')
        }),
        ('Planification', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    readonly_fields = ('created_at', 'updated_at')

    list_display = (
        'reason',
        'status',
        'duration_minutes',
        'appointment_date',
    )

    list_filter = ('status', 'appointment_date')

    search_fields = (
        'reason',
        'doctor__username',
        'patient__username',
    )


admin.site.register(Appointment, AppointmentAdminPers)
