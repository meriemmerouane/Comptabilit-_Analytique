"""
Module de génération de devis PDF professionnel
Pour ELCO-BAT SARL
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime, timedelta

class DevisPDF:
    """Génère un devis PDF professionnel"""
    
    def __init__(self):
        self.width, self.height = A4
        self.styles = getSampleStyleSheet()
        self._setup_styles()
    
    def _setup_styles(self):
        """Configure les styles personnalisés"""
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1f3a93'),
            spaceAfter=6,
            fontName='Helvetica-Bold'
        )
        
        self.heading_style = ParagraphStyle(
            'CustomHeading',
            parent=self.styles['Heading2'],
            fontSize=12,
            textColor=colors.HexColor('#4a7ba7'),
            spaceAfter=12,
            fontName='Helvetica-Bold'
        )
        
        self.normal_style = ParagraphStyle(
            'CustomNormal',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#333333')
        )
    
    def generate(self, donnees):
        """Génère le PDF avec les données du devis"""
        
        buffer = BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=15*mm,
            leftMargin=15*mm,
            topMargin=15*mm,
            bottomMargin=15*mm
        )
        
        story = []
        
        # En-tête
        story.append(self._create_header(donnees))
        story.append(Spacer(1, 10*mm))
        
        # Informations
        story.append(self._create_info_client(donnees))
        story.append(Spacer(1, 10*mm))
        
        # Détail du devis
        story.append(self._create_detail_devis(donnees))
        story.append(Spacer(1, 15*mm))
        
        # Montants
        story.append(self._create_montants(donnees))
        story.append(Spacer(1, 15*mm))
        
        # Conditions
        story.append(self._create_conditions(donnees))
        
        # Footer
        story.append(Spacer(1, 20*mm))
        story.append(self._create_footer())
        
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
    
    def _create_header(self, donnees):
        """Crée l'en-tête du devis"""
        data = [
            [
                Paragraph("<b>ELCO-BAT SARL</b><br/><font size=10>Menuiserie Aluminium</font><br/><font size=8 color='#666'>Tizi Ouzou, Algérie</font>", self.normal_style),
                Paragraph(f"<b style='font-size:18'>DEVIS</b><br/><font size=11><b>N° {donnees['numero_devis']}</b></font>", self.heading_style),
            ]
        ]
        
        table = Table(data, colWidths=[10*cm, 5*cm])
        table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ]))
        
        return table
    
    def _create_info_client(self, donnees):
        """Crée les informations du client et du devis"""
        
        date_emission = datetime.now()
        date_validite = date_emission + timedelta(days=30)
        
        data = [
            [
                Paragraph(f"<b>Référence:</b> {donnees['numero_devis']}", self.normal_style),
                Paragraph(f"<b>Date d'émission:</b> {date_emission.strftime('%d/%m/%Y')}", self.normal_style),
            ],
            [
                Paragraph(f"<b>Client:</b> {donnees.get('client', 'Non renseigné')}", self.normal_style),
                Paragraph(f"<b>Validité:</b> {date_validite.strftime('%d/%m/%Y')}", self.normal_style),
            ],
            [
                Paragraph(f"<b>Adresse:</b> {donnees.get('adresse', '')}", self.normal_style),
                Paragraph(f"<b>Téléphone:</b> {donnees.get('telephone', '')}", self.normal_style),
            ],
            [
                Paragraph(f"<b>Email:</b> {donnees.get('email', '')}", self.normal_style),
                Paragraph(f"<b>Lieu de Livraison:</b> {donnees.get('lieu_livraison', 'Boumerdès')}", self.normal_style),
            ]
        ]
        
        table = Table(data, colWidths=[9*cm, 6*cm])
        table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]))
        
        return table
    
    def _create_detail_devis(self, donnees):
        """Crée le tableau du produit final"""
        
        data = [
            [
                Paragraph("<b>Désignation</b>", self.normal_style),
                Paragraph("<b>Quantité</b>", ParagraphStyle('Center', parent=self.normal_style, alignment=1)),
                Paragraph("<b>Prix unitaire HT</b>", ParagraphStyle('Right', parent=self.normal_style, alignment=2)),
                Paragraph("<b>Total HT</b>", ParagraphStyle('Right', parent=self.normal_style, alignment=2)),
            ]
        ]
        
        # Produit final
        data.append([
            Paragraph("Ensemble menuiserie aluminium<br/><font size=9 color='#666'>Profilés alu + vitrage + quincaillerie inclus</font>", self.normal_style),
            Paragraph("120", ParagraphStyle('Center', parent=self.normal_style, alignment=1)),
            Paragraph(f"{donnees['prix_unitaire']:,.0f} DA", ParagraphStyle('Right', parent=self.normal_style, alignment=2)),
            Paragraph(f"{donnees['prix_vente']:,.0f} DA", ParagraphStyle('Right', parent=self.normal_style, alignment=2)),
        ])
        
        table = Table(data, colWidths=[6*cm, 2*cm, 3*cm, 3*cm])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f3a93')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (0, -1), 'LEFT'),
            ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('TOPPADDING', (0, 0), (-1, 0), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#ddd')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white]),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 1), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 12),
        ]))
        
        return table
    
    def _create_montants(self, donnees):
        """Crée le récapitulatif des montants avec TVA"""
        
        total_ht = donnees['prix_vente']
        tva_rate = 0.19
        tva = total_ht * tva_rate
        total_ttc = total_ht + tva
        
        data = [
            [
                Paragraph("Total HT", self.normal_style),
                Paragraph(f"{total_ht:,.0f} DA", ParagraphStyle('Right', parent=self.normal_style, alignment=2)),
            ],
            [
                Paragraph("TVA (19%)", self.normal_style),
                Paragraph(f"{tva:,.0f} DA", ParagraphStyle('Right', parent=self.normal_style, alignment=2)),
            ],
            [
                Paragraph("<b>Total TTC</b>", ParagraphStyle('Bold', parent=self.normal_style, fontName='Helvetica-Bold')),
                Paragraph(f"<b>{total_ttc:,.0f} DA</b>", ParagraphStyle('BoldRight', parent=self.normal_style, alignment=2, fontName='Helvetica-Bold')),
            ],
        ]
        
        table = Table(data, colWidths=[10*cm, 4*cm])
        table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (0, -1), 'LEFT'),
            ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
            ('FONTNAME', (0, 2), (-1, 2), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 2), (-1, 2), 11),
            ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#e8e8e8')),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#ddd')),
        ]))
        
        return table
    
    def _create_conditions(self, donnees):
        """Crée les conditions du devis"""
        
        conditions = [
            "<b>Conditions générales</b>",
            "— Validité du devis : 30 jours",
            "— Délai de livraison : 45 jours après confirmation",
            "— Acompte : 50% à la commande",
            "— Solde : à la réception",
            "— Garantie : 2 ans pièces et main d'œuvre",
            "— Fourniture complète, montage non compris",
        ]
        
        text = "<br/>".join(conditions)
        return Paragraph(text, ParagraphStyle('Conditions', parent=self.normal_style, fontSize=9, textColor=colors.HexColor('#333')))
    
    def _create_footer(self):
        """Crée le footer du devis"""
        return Paragraph(
            "<font size=8 color='#999'>ELCO-BAT SARL • Menuiserie Aluminium • Tizi Ouzou<br/>"
            f"Devis généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')} • "
            "Ce document est un devis professionnel</font>",
            ParagraphStyle('Footer', parent=self.normal_style, alignment=1, fontSize=8)
        )


def creer_pdf_devis(donnees):
    """Fonction utilitaire pour créer rapidement un PDF devis"""
    pdf_gen = DevisPDF()
    return pdf_gen.generate(donnees)


# Support des imports pour les mesures
from reportlab.lib.units import cm
