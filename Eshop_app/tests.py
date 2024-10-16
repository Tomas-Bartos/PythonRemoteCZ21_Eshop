from django.test import TestCase
from django.urls import reverse
from Eshop_app.models import Product, Category, User

# test registrace a přihlášení uživatele
class UserAuthTests(TestCase):
    def test_registration(self):
        # Simulace POST požadavku pro registraci
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'country': 'Test Country',  # Přidejte další povinné pole
            'city': 'Test City',
            'street': 'Test Street',
            'zip': '12345',
        })

        # Ověření správné registrace
        if response.status_code == 200:
            print(response.context['form'].errors)

        self.assertEqual(response.status_code, 302)  # Očekáváme přesměrování
        self.assertTrue(User.objects.filter(username='testuser').exists())  # Ověření, že uživatel byl vytvořen
        self.assertRedirects(response, reverse('user'))  # Ověření, že došlo k přesměrování na správnou stránku

    def test_registration_with_password_mismatch(self):
        # Simulace POST požadavku pro registraci s nesouladem hesel
        response = self.client.post(reverse('register'), {
            'username': 'testuser2',
            'email': 'test2@example.com',
            'password1': 'testpass123',
            'password2': 'wrongpassword',  # Zde hesla nesouhlasí
        })

        # Ověření, že došlo k chybě a uživatel nebyl vytvořen
        self.assertEqual(response.status_code, 200)  # Očekáváme, že se stránka znovu načte
        self.assertFalse(User.objects.filter(username='testuser2').exists())  # Ověření, že uživatel nebyl vytvořen

        # Ověření, že formulář obsahuje chyby
        form = response.context['form']
        self.assertTrue(form.errors)

    def test_login(self):
        User.objects.create_user(username='testuser', password='testpass123')
        # simulace POST požadavku pro přihlášení
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123',
        })
        # ověření správného přihlášení
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)


#test pro nákupní košík
class SessionCartTests(TestCase):
    def setUp(self):
        # vytvoření kategorie a produktu
        self.category = Category.objects.create(name='Test Category')  # Přidání kategorie
        self.product = Product.objects.create(name='Test Product', price=5.00, category=self.category)

    def test_add_to_cart(self):
        # simulace přidání do košíku
        response = self.client.post(reverse('add_to_cart'), {
            'product_id': self.product.id,
        })
        # ověření přidání produktu do košíku session
        self.assertEqual(response.status_code, 302)
        cart = self.client.session.get('cart_view', {})
        self.assertIn(str(self.product.id), cart)
        self.assertEqual(cart[str(self.product.id)]['quantity'], 1)

    def test_remove_from_cart(self):
        # Přidání produktu do košíku
        self.client.post(reverse('add_to_cart'), {'product_id': self.product.id})

        # Simulace odstranění produktu z košíku
        response = self.client.post(reverse('remove_from_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)

        # Ověření, že produkt byl odstraněn ze session
        cart = self.client.session.get('cart_view', {})
        self.assertNotIn(str(self.product.id), cart)  # Ujistit se, že produkt není v košíku
