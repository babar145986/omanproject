import qrcode
from django.db import models
from django.core.files.base import ContentFile
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class AddRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    date_of_contract = models.CharField(max_length=120, default="20/05/2023")
    contract_number = models.CharField(max_length=120, default="1065732")
    usage_type = models.CharField(max_length=120, null=True, blank=True, default=" تجاري ")
    contract_starting_date = models.CharField(max_length=120, default="20/05/2024")
    contract_expiry_date = models.CharField(max_length=120, default="19/05/2024")
    monthly_rent = models.CharField(max_length=120, null=True, blank=True, default="10")
    contract_fees = models.CharField(max_length=120, null=True, blank=True, default="366")
    rented_loom = models.CharField(max_length=120, null=True, blank=True, default="شرکة")
    rented_loom2 = models.CharField(max_length=120, null=True, blank=True, default="شرکة")
    name = models.CharField(max_length=120, null=True, blank=True, default=" مجدى بن مستهيل بن منجور جعبوب ")
    name_2 = models.CharField(max_length=120, null=True, blank=True, default="مؤسسة سحابة شمال الشرقي المتميز للتجارة والمقاولات")
    khaif_no = models.CharField(max_length=120, null=True, blank=True, default="1341270")
    card_no = models.CharField(max_length=120, default="5413313")
    commercial_register = models.CharField(max_length=120, null=True, blank=True, default="1396496")
    commercial_register_2 = models.CharField(max_length=120, null=True, blank=True, default="0000000")
    nationality = models.CharField(max_length=120, null=True, blank=True, default="عمان")
    field_type = models.CharField(max_length=120, null=True, blank=True, default="صلالة")
    state = models.CharField(max_length=120, null=True, blank=True, default="")
    street = models.CharField(max_length=120, null=True, blank=True, default="")
    almatqatu = models.CharField(max_length=120, default="الصناعيات الجديدة")
    electricity_account_number = models.CharField(max_length=120, null=True, blank=True, default="2862682")
    property_type = models.CharField(max_length=120, null=True, blank=True, default="")
    phone_number2 = models.CharField(max_length=120, null=True, blank=True, default="92792776")
    phone_number = models.CharField(max_length=120, null=True, blank=True, default="72582037")
    vichle_mechanic_repair = models.CharField(max_length=120, null=True, blank=True, default="452002")
    profession = models.CharField(max_length=120, default=" إصلاح ميكانيك المركبات", null=True, blank=True)
    profession2 = models.CharField(max_length=120, null=True, blank=True)
    vichle_mechanic_repair2 = models.CharField(max_length=120, null=True, blank=True)
    raqmul_qareebi = models.CharField(max_length=120, null=True, blank=True, default="0")
    raqmul_qatga = models.CharField(max_length=120, null=True, blank=True, default="125")
    qr_code = models.ImageField(upload_to="media/qr_code", null=True, blank=True)
    street = models.CharField(max_length=120, null=True, blank=True, default="شارغ عام")
    block = models.CharField(max_length=120, null=True, blank=True, default="ب")

    def generate_qr_code(self):
        qr_code_content = f"https://www.appedmgovt.com/single_record/{self.id}"
        qr_code_image = qrcode.make(qr_code_content)
        buffer = BytesIO()
        qr_code_image.save(buffer, format='PNG')
        buffer.seek(0)
        filename = f"qr_code_{self.id}.png"
        file = InMemoryUploadedFile(
            buffer, None, filename, 'image/png', buffer.getbuffer().nbytes, None
        )
        return file

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)

        if not self.qr_code:  # Check if the QR code field is empty
            qr_code_file = self.generate_qr_code()
            if qr_code_file:
                self.qr_code.save(qr_code_file.name, qr_code_file, save=True)

        super().save(*args, **kwargs)