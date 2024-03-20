from django.db import models

class descMovimenti(models.Model):
    descrizione = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.descrizione

class Giornaliero(models.Model):
    data = models.DateField()
    descrizione = models.CharField(max_length=100, null=True, blank=True)
    totaleCassa = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    incassoPresunto = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    differenza = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.data, self.descrizione
    

class Image(models.Model):
    giornaliero = models.ForeignKey(Giornaliero, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.giornaliero.data
    

class Dettagli(models.Model):
    tipoMovimento = descMovimenti.objects.all()
    '''tipoMovimento = ( 
        ('TABACCHI', 'TABACCHI'), 
        ('LOTTO', 'LOTTO'),
        ('ART. TABACCHERIA', 'ART. TABACCHERIA'),
        ('SISAL', 'SISAL'),
        ('GRATTA E VINCI', 'GRATTA E VINCI'),
        ('ALTRE USCITE', 'ALTRE USCITE'),
        ('PASTIGLIAGGI', 'PASTIGLIAGGI'),
        ('VALORI BOLLATI', 'VALORI BOLLATI'),
    ) ''' 
    giornaliero = models.ForeignKey(Giornaliero, on_delete=models.CASCADE)
    movimento = models.ForeignKey(descMovimenti, on_delete=models.CASCADE)
    '''movimento = models.CharField(max_length=100, choices=tipoMovimento)'''
    entrata = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    uscita = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.giornaliero.data
    
