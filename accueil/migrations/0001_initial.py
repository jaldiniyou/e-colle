# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-12 09:55
from __future__ import unicode_literals

import accueil.models
import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30, unique=True)),
                ('annee', models.PositiveSmallIntegerField(choices=[(1, '1ère année'), (2, '2ème année')], default=1)),
            ],
            options={
                'ordering': ['annee', 'nom'],
            },
        ),
        migrations.CreateModel(
            name='Colle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accueil.Classe')),
            ],
        ),
        migrations.CreateModel(
            name='Colleur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveSmallIntegerField(choices=[(0, 'autre'), (1, 'certifié'), (2, 'bi-admissible'), (3, 'agrégé'), (4, 'chaire supérieure')], default=3)),
                ('classes', models.ManyToManyField(to='accueil.Classe', verbose_name='Classe(s)')),
            ],
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_etablissement', models.CharField(blank=True, max_length=30, verbose_name="Nom de l'établissement")),
                ('modif_secret_col', models.BooleanField(verbose_name='Modification du colloscope par le secrétariat')),
                ('modif_secret_groupe', models.BooleanField(verbose_name='Modification des groupes par le secrétariat')),
                ('modif_prof_col', models.BooleanField(verbose_name='Modification du colloscope par les enseignants')),
                ('default_modif_col', models.BooleanField(verbose_name='Modification du colloscope par défaut pour tous les enseignants')),
                ('modif_prof_groupe', models.BooleanField(verbose_name='Modification des groupes par les enseignants')),
                ('default_modif_groupe', models.BooleanField(verbose_name='Modification des groupes par défaut pour tous les enseignants')),
                ('mathjax', models.BooleanField(verbose_name='Mise en forme des formules mathématiques avec Mathjax')),
                ('ects', models.BooleanField(verbose_name='Gestion des fiches de crédits ECTS')),
                ('nom_adresse_etablissement', models.TextField(blank=True, verbose_name="Nom complet de l'établissement + adresse")),
                ('ville', models.CharField(blank=True, max_length=40, verbose_name="Ville de l'établissement")),
                ('academie', models.CharField(blank=True, max_length=40, verbose_name="Académie de l'établissement")),
            ],
        ),
        migrations.CreateModel(
            name='Creneau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.PositiveSmallIntegerField(choices=[(0, 'lundi'), (1, 'mardi'), (2, 'mercredi'), (3, 'jeudi'), (4, 'vendredi'), (5, 'samedi')], default=0)),
                ('heure', models.PositiveSmallIntegerField(choices=[(24, '6h00'), (25, '6h15'), (26, '6h30'), (27, '6h45'), (28, '7h00'), (29, '7h15'), (30, '7h30'), (31, '7h45'), (32, '8h00'), (33, '8h15'), (34, '8h30'), (35, '8h45'), (36, '9h00'), (37, '9h15'), (38, '9h30'), (39, '9h45'), (40, '10h00'), (41, '10h15'), (42, '10h30'), (43, '10h45'), (44, '11h00'), (45, '11h15'), (46, '11h30'), (47, '11h45'), (48, '12h00'), (49, '12h15'), (50, '12h30'), (51, '12h45'), (52, '13h00'), (53, '13h15'), (54, '13h30'), (55, '13h45'), (56, '14h00'), (57, '14h15'), (58, '14h30'), (59, '14h45'), (60, '15h00'), (61, '15h15'), (62, '15h30'), (63, '15h45'), (64, '16h00'), (65, '16h15'), (66, '16h30'), (67, '16h45'), (68, '17h00'), (69, '17h15'), (70, '17h30'), (71, '17h45'), (72, '18h00'), (73, '18h15'), (74, '18h30'), (75, '18h45'), (76, '19h00'), (77, '19h15'), (78, '19h30'), (79, '19h45'), (80, '20h00'), (81, '20h15'), (82, '20h30'), (83, '20h45'), (84, '21h00'), (85, '21h15'), (86, '21h30'), (87, '21h45'), (88, '22h00')], default=24)),
                ('salle', models.CharField(blank=True, max_length=20, null=True)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classecreneau', to='accueil.Classe')),
            ],
            options={
                'ordering': ['jour', 'heure', 'salle', 'pk'],
            },
        ),
        migrations.CreateModel(
            name='Destinataire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lu', models.BooleanField(default=False)),
                ('reponses', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=accueil.models.Eleve.update_photo, verbose_name='photo(jpg/png, 300x400)')),
                ('ddn', models.DateField(blank=True, null=True, verbose_name='Date de naissance')),
                ('ldn', models.CharField(blank=True, default='', max_length=50, verbose_name='Lieu de naissance')),
                ('ine', models.CharField(blank=True, max_length=11, null=True, verbose_name='numéro étudiant (INE)')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='classeeleve', to='accueil.Classe')),
            ],
            options={
                'ordering': ['user__last_name', 'user__first_name'],
            },
        ),
        migrations.CreateModel(
            name='Etablissement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=2)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='classegroupe', to='accueil.Classe')),
            ],
            options={
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='JourFerie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('couleur', models.CharField(choices=[('#696969', 'Gris mat'), ('#808080', 'Gris'), ('#A9A9A9', 'Gris foncé'), ('#C0C0C0', 'Gris argent'), ('#D3D3D3', 'Gris clair'), ('#DCDCDC', 'Gris Gainsboro'), ('#FFC0CB', 'Rose'), ('#FFB6C1', 'Rose clair'), ('#FF69B4', 'Rose passion'), ('#FF1493', 'Rose profond'), ('#DB7093', 'Violet Pâle'), ('#FF00FF', 'Fushia'), ('#C71585', 'Violet moyen'), ('#D8BFD8', 'Violet chardon'), ('#DDA0DD', 'Prune'), ('#EE82EE', 'Violet'), ('#DA70D6', 'Orchidée'), ('#9932CC', 'Orchidée foncé'), ('#9400D3', 'Violet foncé'), ('#8A2BE2', 'Bleu violet'), ('#4B0082', 'Indigo'), ('#7B68EE', 'Bleu ardoise moyen'), ('#6A5ACD', 'Bleu ardoise'), ('#483D8B', 'Bleu ardoise foncé'), ('#9370DB', 'Pourpre moyen'), ('#8B008B', 'Magenta foncé'), ('#800080', 'Pourpre'), ('#BC8F8F', 'Brun rosé'), ('#F08080', 'Corail clair'), ('#FF7F50', 'Corail'), ('#FF6347', 'Tomate'), ('#FF4500', 'Orangé'), ('#FF0000', 'Rouge'), ('#DC143C', 'Rouge cramoisi'), ('#FFA07A', 'Saumon clair'), ('#E9967A', 'Saumon foncé'), ('#FA8072', 'Saumon'), ('#CD5C5C', 'Rouge indien'), ('#B22222', 'Rouge brique'), ('#A52A2A', 'Marron'), ('#8B0000', 'Rouge foncé'), ('#800000', 'Bordeaux'), ('#DEB887', 'Brun bois'), ('#D2B48C', 'Brun roux'), ('#F4A460', 'Brun sable'), ('#FFA500', 'Orange'), ('#FF8C00', 'Orange foncé'), ('#D2691E', 'Chocolat'), ('#CD853F', 'Brun péro'), ('#A0522D', 'Terre de Sienne'), ('#8B4513', 'Brun cuir'), ('#F0E68C', 'Brun kaki'), ('#FFFF00', 'Jaune'), ('#FFD700', 'Or'), ('#DAA520', 'Jaune doré'), ('#B8860B', 'Jaune doré foncé'), ('#BDB76B', 'Brun kaki foncé'), ('#9ACD32', 'Jaune vert'), ('#6B8E23', 'Kaki'), ('#808000', 'Olive'), ('#556B2F', 'Olive foncé'), ('#ADFF2F', 'Vert jaune'), ('#7FFF00', 'Chartreuse'), ('#7CFC00', 'Vert prairie'), ('#00FF00', 'Cirton vert'), ('#32CD32', 'Citron vers foncé'), ('#98FB98', 'Vert pâle'), ('#90EE90', 'Vert clair'), ('#00FF7F', 'Vert printemps'), ('#00FA9A', 'Vert printemps mpyen'), ('#228B22', 'Vert forêt'), ('#008000', 'Vert'), ('#006400', 'Vert foncé'), ('#8FBC8F', 'Vert océan foncé'), ('#3CB371', 'Vert océan moyen'), ('#2E8B57', 'Vert océan'), ('#778899', 'Gris aroise clair'), ('#708090', 'Gris ardoise'), ('#2F4F4F', 'Gris ardoise foncé'), ('#7FFFD4', 'Aigue-marine'), ('#66CDAA', 'Aigue-marine moyen'), ('#00FFFF', 'Cyan'), ('#40E0D0', 'Turquoise'), ('#48D1CC', 'Turquoise moyen'), ('#00CED1', 'Turquoise foncé'), ('#20B2AA', 'Vert marin clair'), ('#008B8B', 'Cyan foncé'), ('#008080', 'Vert sarcelle'), ('#5F9EA0', 'Bleu pétrole'), ('#B0E0E6', 'Bleu poudre'), ('#ADD8E6', 'Bleu clair'), ('#87CEFA', 'Bleu azur clair'), ('#87CEEB', 'Bleu azur'), ('#00BFFF', 'Bleu azur profond'), ('#1E90FF', 'Bleu toile'), ('#B0C4DE', 'Bleu acier clair'), ('#6495ED', 'Bleuet'), ('#4682B4', 'Bleu acier'), ('#4169E1', 'Bleu royal'), ('#0000FF', 'Bleu'), ('#0000CD', 'Bleu moyen'), ('#00008B', 'Bleu foncé'), ('#000080', 'Bleu marin'), ('#191970', 'Bleu de minuit')], default='#696969', max_length=7)),
                ('temps', models.PositiveSmallIntegerField(choices=[(20, '20 min (par groupe de 3)'), (30, '30 min (solo)'), (60, '60 min (informatique)')], default=20, verbose_name='minutes/colle/élève')),
                ('lv', models.PositiveSmallIntegerField(choices=[(0, '---'), (1, 'LV1'), (2, 'LV2')], default=0, verbose_name='Langue vivante')),
            ],
            options={
                'ordering': ['nom', 'lv', 'temps'],
            },
        ),
        migrations.CreateModel(
            name='MatiereECTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=80, verbose_name='Matière')),
                ('precision', models.CharField(blank=True, max_length=20, verbose_name='Précision')),
                ('semestre1', models.PositiveSmallIntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20)], null=True, verbose_name='coefficient semestre 1')),
                ('semestre2', models.PositiveSmallIntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20)], null=True, verbose_name='coefficient semestre 2')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classematiereECTS', to='accueil.Classe', verbose_name='Classe')),
                ('profs', models.ManyToManyField(blank=True, related_name='colleurmatiereECTS', to='accueil.Colleur', verbose_name='Professeur')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hasAuteur', models.BooleanField(default=True)),
                ('luPar', models.TextField(verbose_name='lu par: ')),
                ('listedestinataires', models.TextField(verbose_name='Liste des destinataires')),
                ('titre', models.CharField(max_length=100)),
                ('corps', models.TextField(max_length=2000)),
                ('auteur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messagesenvoyes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enreg', models.DateField(auto_now_add=True)),
                ('date_colle', models.DateField(default=datetime.date.today, verbose_name='date de rattrapage')),
                ('rattrapee', models.BooleanField(verbose_name='rattrapée')),
                ('jour', models.PositiveSmallIntegerField(choices=[(0, 'lundi'), (1, 'mardi'), (2, 'mercredi'), (3, 'jeudi'), (4, 'vendredi'), (5, 'samedi')], default=0)),
                ('note', models.PositiveSmallIntegerField(choices=[(21, 'n.n'), (22, 'Abs'), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20)], default=22)),
                ('heure', models.PositiveSmallIntegerField(choices=[(24, '6h00'), (25, '6h15'), (26, '6h30'), (27, '6h45'), (28, '7h00'), (29, '7h15'), (30, '7h30'), (31, '7h45'), (32, '8h00'), (33, '8h15'), (34, '8h30'), (35, '8h45'), (36, '9h00'), (37, '9h15'), (38, '9h30'), (39, '9h45'), (40, '10h00'), (41, '10h15'), (42, '10h30'), (43, '10h45'), (44, '11h00'), (45, '11h15'), (46, '11h30'), (47, '11h45'), (48, '12h00'), (49, '12h15'), (50, '12h30'), (51, '12h45'), (52, '13h00'), (53, '13h15'), (54, '13h30'), (55, '13h45'), (56, '14h00'), (57, '14h15'), (58, '14h30'), (59, '14h45'), (60, '15h00'), (61, '15h15'), (62, '15h30'), (63, '15h45'), (64, '16h00'), (65, '16h15'), (66, '16h30'), (67, '16h45'), (68, '17h00'), (69, '17h15'), (70, '17h30'), (71, '17h45'), (72, '18h00'), (73, '18h15'), (74, '18h30'), (75, '18h45'), (76, '19h00'), (77, '19h15'), (78, '19h30'), (79, '19h45'), (80, '20h00'), (81, '20h15'), (82, '20h30'), (83, '20h45'), (84, '21h00'), (85, '21h15'), (86, '21h30'), (87, '21h45'), (88, '22h00')], default=14)),
                ('commentaire', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Commentaire(facultatif)')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accueil.Classe')),
                ('colleur', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accueil.Colleur')),
                ('eleve', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accueil.Eleve')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accueil.Matiere')),
            ],
        ),
        migrations.CreateModel(
            name='NoteECTS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestre', models.PositiveSmallIntegerField(choices=[(1, '1er semestre'), (2, '2ème semestre')], verbose_name='semestre')),
                ('note', models.PositiveSmallIntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E'), (5, 'F')])),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.Eleve', verbose_name='Élève')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.MatiereECTS')),
            ],
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modifgroupe', models.BooleanField(verbose_name='Droits de modification des groupes de colle')),
                ('modifcolloscope', models.BooleanField(verbose_name='Droits de modification du colloscope')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classeprof', to='accueil.Classe', verbose_name='Classe')),
                ('colleur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colleurprof', to='accueil.Colleur', verbose_name='Professeur')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matiereprof', to='accueil.Matiere', verbose_name='Matière')),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('detail', models.TextField(blank=True, null=True, verbose_name='Détails')),
                ('fichier', models.FileField(blank=True, null=True, upload_to=accueil.models.Programme.update_name, verbose_name='Fichier(pdf)')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='classeprogramme', to='accueil.Classe')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='matiereprogramme', to='accueil.Matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Ramassage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moisDebut', models.DateField(choices=[(datetime.date(2017, 9, 1), 'septembre 2017')], verbose_name='Début')),
                ('moisFin', models.DateField(choices=[(datetime.date(2017, 9, 1), 'septembre 2017')], verbose_name='Fin')),
            ],
            options={
                'ordering': ['moisDebut', 'moisFin'],
            },
        ),
        migrations.CreateModel(
            name='Semaine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35)], default=1, unique=True)),
                ('lundi', models.DateField(choices=[(datetime.date(2016, 12, 5), '05 décembre 2016'), (datetime.date(2016, 12, 12), '12 décembre 2016'), (datetime.date(2016, 12, 19), '19 décembre 2016'), (datetime.date(2016, 12, 26), '26 décembre 2016'), (datetime.date(2017, 1, 2), '02 janvier 2017'), (datetime.date(2017, 1, 9), '09 janvier 2017'), (datetime.date(2017, 1, 16), '16 janvier 2017'), (datetime.date(2017, 1, 23), '23 janvier 2017'), (datetime.date(2017, 1, 30), '30 janvier 2017'), (datetime.date(2017, 2, 6), '06 février 2017'), (datetime.date(2017, 2, 13), '13 février 2017'), (datetime.date(2017, 2, 20), '20 février 2017'), (datetime.date(2017, 2, 27), '27 février 2017'), (datetime.date(2017, 3, 6), '06 mars 2017'), (datetime.date(2017, 3, 13), '13 mars 2017'), (datetime.date(2017, 3, 20), '20 mars 2017'), (datetime.date(2017, 3, 27), '27 mars 2017'), (datetime.date(2017, 4, 3), '03 avril 2017'), (datetime.date(2017, 4, 10), '10 avril 2017'), (datetime.date(2017, 4, 17), '17 avril 2017'), (datetime.date(2017, 4, 24), '24 avril 2017'), (datetime.date(2017, 5, 1), '01 mai 2017'), (datetime.date(2017, 5, 8), '08 mai 2017'), (datetime.date(2017, 5, 15), '15 mai 2017'), (datetime.date(2017, 5, 22), '22 mai 2017'), (datetime.date(2017, 5, 29), '29 mai 2017'), (datetime.date(2017, 6, 5), '05 juin 2017'), (datetime.date(2017, 6, 12), '12 juin 2017'), (datetime.date(2017, 6, 19), '19 juin 2017'), (datetime.date(2017, 6, 26), '26 juin 2017'), (datetime.date(2017, 7, 3), '03 juillet 2017'), (datetime.date(2017, 7, 10), '10 juillet 2017'), (datetime.date(2017, 7, 17), '17 juillet 2017'), (datetime.date(2017, 7, 24), '24 juillet 2017'), (datetime.date(2017, 7, 31), '31 juillet 2017'), (datetime.date(2017, 8, 7), '07 août 2017'), (datetime.date(2017, 8, 14), '14 août 2017'), (datetime.date(2017, 8, 21), '21 août 2017'), (datetime.date(2017, 8, 28), '28 août 2017'), (datetime.date(2017, 9, 4), '04 septembre 2017'), (datetime.date(2017, 9, 11), '11 septembre 2017'), (datetime.date(2017, 9, 18), '18 septembre 2017'), (datetime.date(2017, 9, 25), '25 septembre 2017'), (datetime.date(2017, 10, 2), '02 octobre 2017'), (datetime.date(2017, 10, 9), '09 octobre 2017'), (datetime.date(2017, 10, 16), '16 octobre 2017'), (datetime.date(2017, 10, 23), '23 octobre 2017'), (datetime.date(2017, 10, 30), '30 octobre 2017'), (datetime.date(2017, 11, 6), '06 novembre 2017'), (datetime.date(2017, 11, 13), '13 novembre 2017'), (datetime.date(2017, 11, 20), '20 novembre 2017'), (datetime.date(2017, 11, 27), '27 novembre 2017'), (datetime.date(2017, 12, 4), '04 décembre 2017'), (datetime.date(2017, 12, 11), '11 décembre 2017'), (datetime.date(2017, 12, 18), '18 décembre 2017'), (datetime.date(2017, 12, 25), '25 décembre 2017'), (datetime.date(2018, 1, 1), '01 janvier 2018'), (datetime.date(2018, 1, 8), '08 janvier 2018'), (datetime.date(2018, 1, 15), '15 janvier 2018'), (datetime.date(2018, 1, 22), '22 janvier 2018'), (datetime.date(2018, 1, 29), '29 janvier 2018'), (datetime.date(2018, 2, 5), '05 février 2018'), (datetime.date(2018, 2, 12), '12 février 2018'), (datetime.date(2018, 2, 19), '19 février 2018'), (datetime.date(2018, 2, 26), '26 février 2018'), (datetime.date(2018, 3, 5), '05 mars 2018'), (datetime.date(2018, 3, 12), '12 mars 2018'), (datetime.date(2018, 3, 19), '19 mars 2018'), (datetime.date(2018, 3, 26), '26 mars 2018'), (datetime.date(2018, 4, 2), '02 avril 2018'), (datetime.date(2018, 4, 9), '09 avril 2018'), (datetime.date(2018, 4, 16), '16 avril 2018'), (datetime.date(2018, 4, 23), '23 avril 2018'), (datetime.date(2018, 4, 30), '30 avril 2018'), (datetime.date(2018, 5, 7), '07 mai 2018'), (datetime.date(2018, 5, 14), '14 mai 2018'), (datetime.date(2018, 5, 21), '21 mai 2018'), (datetime.date(2018, 5, 28), '28 mai 2018'), (datetime.date(2018, 6, 4), '04 juin 2018'), (datetime.date(2018, 6, 11), '11 juin 2018'), (datetime.date(2018, 6, 18), '18 juin 2018'), (datetime.date(2018, 6, 25), '25 juin 2018'), (datetime.date(2018, 7, 2), '02 juillet 2018'), (datetime.date(2018, 7, 9), '09 juillet 2018'), (datetime.date(2018, 7, 16), '16 juillet 2018'), (datetime.date(2018, 7, 23), '23 juillet 2018'), (datetime.date(2018, 7, 30), '30 juillet 2018'), (datetime.date(2018, 8, 6), '06 août 2018'), (datetime.date(2018, 8, 13), '13 août 2018'), (datetime.date(2018, 8, 20), '20 août 2018'), (datetime.date(2018, 8, 27), '27 août 2018'), (datetime.date(2018, 9, 3), '03 septembre 2018'), (datetime.date(2018, 9, 10), '10 septembre 2018'), (datetime.date(2018, 9, 17), '17 septembre 2018'), (datetime.date(2018, 9, 24), '24 septembre 2018'), (datetime.date(2018, 10, 1), '01 octobre 2018'), (datetime.date(2018, 10, 8), '08 octobre 2018'), (datetime.date(2018, 10, 15), '15 octobre 2018'), (datetime.date(2018, 10, 22), '22 octobre 2018'), (datetime.date(2018, 10, 29), '29 octobre 2018')], default=datetime.date(2017, 9, 11), unique=True)),
            ],
            options={
                'ordering': ['lundi'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='ramassage',
            unique_together=set([('moisDebut', 'moisFin')]),
        ),
        migrations.AddField(
            model_name='programme',
            name='semaine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='semaineprogramme', to='accueil.Semaine'),
        ),
        migrations.AddField(
            model_name='note',
            name='semaine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='semainenote', to='accueil.Semaine'),
        ),
        migrations.AlterUniqueTogether(
            name='matiere',
            unique_together=set([('nom', 'lv', 'temps')]),
        ),
        migrations.AddField(
            model_name='eleve',
            name='groupe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groupeeleve', to='accueil.Groupe'),
        ),
        migrations.AddField(
            model_name='eleve',
            name='lv1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elevelv1', to='accueil.Matiere'),
        ),
        migrations.AddField(
            model_name='eleve',
            name='lv2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elevelv2', to='accueil.Matiere'),
        ),
        migrations.AddField(
            model_name='destinataire',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messagerecu', to='accueil.Message'),
        ),
        migrations.AddField(
            model_name='destinataire',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinataire', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='colleur',
            name='etablissement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accueil.Etablissement', verbose_name='Établissement'),
        ),
        migrations.AddField(
            model_name='colleur',
            name='matieres',
            field=models.ManyToManyField(to='accueil.Matiere', verbose_name='Matière(s)'),
        ),
        migrations.AddField(
            model_name='colle',
            name='colleur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accueil.Colleur'),
        ),
        migrations.AddField(
            model_name='colle',
            name='creneau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accueil.Creneau'),
        ),
        migrations.AddField(
            model_name='colle',
            name='eleve',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accueil.Eleve'),
        ),
        migrations.AddField(
            model_name='colle',
            name='groupe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accueil.Groupe'),
        ),
        migrations.AddField(
            model_name='colle',
            name='matiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accueil.Matiere'),
        ),
        migrations.AddField(
            model_name='colle',
            name='semaine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accueil.Semaine'),
        ),
        migrations.AddField(
            model_name='classe',
            name='matieres',
            field=models.ManyToManyField(blank=True, related_name='matieresclasse', to='accueil.Matiere', verbose_name='matières'),
        ),
        migrations.AddField(
            model_name='classe',
            name='profprincipal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classeprofprincipal', to='accueil.Colleur'),
        ),
        migrations.AddField(
            model_name='user',
            name='colleur',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accueil.Colleur'),
        ),
        migrations.AddField(
            model_name='user',
            name='eleve',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accueil.Eleve'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='programme',
            unique_together=set([('semaine', 'classe', 'matiere')]),
        ),
        migrations.AlterUniqueTogether(
            name='prof',
            unique_together=set([('classe', 'matiere')]),
        ),
        migrations.AlterUniqueTogether(
            name='noteects',
            unique_together=set([('eleve', 'matiere', 'semestre')]),
        ),
        migrations.AlterUniqueTogether(
            name='matiereects',
            unique_together=set([('classe', 'nom', 'precision')]),
        ),
        migrations.AlterUniqueTogether(
            name='groupe',
            unique_together=set([('nom', 'classe')]),
        ),
    ]
