# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Albums(models.Model):
    albumid = models.IntegerField(db_column='AlbumId', primary_key=True)
    title = models.TextField(db_column='Title')
    artistid = models.IntegerField(db_column='ArtistId')

    class Meta:
        managed = False
        db_table = 'albums'


class Artists(models.Model):
    artistid = models.IntegerField(db_column='ArtistId', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artists'


class Customers(models.Model):
    customerid = models.IntegerField(db_column='CustomerId', primary_key=True)
    firstname = models.TextField(db_column='FirstName')
    lastname = models.TextField(db_column='LastName')
    company = models.TextField(db_column='Company', blank=True, null=True)
    address = models.TextField(db_column='Address', blank=True, null=True)
    city = models.TextField(db_column='City', blank=True, null=True)
    state = models.TextField(db_column='State', blank=True, null=True)
    country = models.TextField(db_column='Country', blank=True, null=True)
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)
    phone = models.TextField(db_column='Phone', blank=True, null=True)
    fax = models.TextField(db_column='Fax', blank=True, null=True)
    email = models.TextField(db_column='Email')
    supportrepid = models.IntegerField(db_column='SupportRepId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Employees(models.Model):
    employeeid = models.IntegerField(db_column='EmployeeId', primary_key=True)
    lastname = models.TextField(db_column='LastName')
    firstname = models.TextField(db_column='FirstName')
    title = models.TextField(db_column='Title', blank=True, null=True)
    reportsto = models.IntegerField(db_column='ReportsTo', blank=True, null=True)
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True)
    address = models.TextField(db_column='Address', blank=True, null=True)
    city = models.TextField(db_column='City', blank=True, null=True)
    state = models.TextField(db_column='State', blank=True, null=True)
    country = models.TextField(db_column='Country', blank=True, null=True)
    postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)
    phone = models.TextField(db_column='Phone', blank=True, null=True)
    fax = models.TextField(db_column='Fax', blank=True, null=True)
    email = models.TextField(db_column='Email', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class Genres(models.Model):
    genreid = models.IntegerField(db_column='GenreId', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genres'


class InvoiceItems(models.Model):
    invoicelineid = models.IntegerField(db_column='InvoiceLineId', primary_key=True)
    invoiceid = models.IntegerField(db_column='InvoiceId')
    trackid = models.IntegerField(db_column='TrackId')
    unitprice = models.TextField(db_column='UnitPrice')
    quantity = models.IntegerField(db_column='Quantity')

    class Meta:
        managed = False
        db_table = 'invoice_items'


class Invoices(models.Model):
    invoiceid = models.IntegerField(db_column='InvoiceId', primary_key=True)
    customerid = models.IntegerField(db_column='CustomerId')
    invoicedate = models.DateTimeField(db_column='InvoiceDate')
    billingaddress = models.TextField(db_column='BillingAddress', blank=True, null=True)
    billingcity = models.TextField(db_column='BillingCity', blank=True, null=True)
    billingstate = models.TextField(db_column='BillingState', blank=True, null=True)
    billingcountry = models.TextField(db_column='BillingCountry', blank=True, null=True)
    billingpostalcode = models.TextField(db_column='BillingPostalCode', blank=True, null=True)
    total = models.TextField(db_column='Total')

    class Meta:
        managed = False
        db_table = 'invoices'


class MediaTypes(models.Model):
    mediatypeid = models.IntegerField(db_column='MediaTypeId', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media_types'


class PlaylistTrack(models.Model):
    playlistid = models.IntegerField(db_column='PlaylistId', primary_key=True)
    trackid = models.IntegerField(db_column='TrackId')

    class Meta:
        managed = False
        db_table = 'playlist_track'
        unique_together = (('playlistid', 'trackid'),)


class Playlists(models.Model):
    playlistid = models.IntegerField(db_column='PlaylistId', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playlists'


class SaleRecords(models.Model):
    salerecordid = models.IntegerField(db_column='SaleRecordId', primary_key=True)
    employeeid = models.IntegerField(db_column='EmployeeId')
    invoiceid = models.IntegerField(db_column='InvoiceId')

    class Meta:
        managed = False
        db_table = 'sale_records'


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True) # 
    idx = models.TextField(blank=True, null=True) # 
    stat = models.TextField(blank=True, null=True) # 

    class Meta:
        managed = False
        db_table = 'sqlite_stat1'


class Tracks(models.Model):
    trackid = models.IntegerField(db_column='TrackId')
    name = models.TextField(db_column='Name')
    albumid = models.IntegerField(db_column='AlbumId', blank=True, null=True)
    mediatypeid = models.IntegerField(db_column='MediaTypeId')
    genreid = models.IntegerField(db_column='GenreId', blank=True, null=True)
    composer = models.TextField(db_column='Composer', blank=True, null=True)
    milliseconds = models.IntegerField(db_column='Milliseconds')
    bytes = models.IntegerField(db_column='Bytes', blank=True, null=True)
    unitprice = models.TextField(db_column='UnitPrice')

    class Meta:
        managed = False
        db_table = 'tracks'
