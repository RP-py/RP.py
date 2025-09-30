class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class ValidadorUsuario:
    @staticmethod
    def validar(usuario):
        if not usuario.nombre or len(usuario.nombre.strip()) == 0:
            raise ValueError("Nombre no puede estar vacío")
        if "@" not in usuario.email:
            raise ValueError("Email inválido")
        return True

class RepositorioUsuario:
    def guardar(self, usuario):
        print(f"Guardando {usuario.nombre} en la base de datos...")
    
    def buscar_por_id(self, id_usuario):
        print(f"Buscando usuario con ID {id_usuario}...")
        return Usuario("Ejemplo", "ejemplo@email.com")

class ServicioEmail:
    def enviar_email_bienvenida(self, usuario):
        print(f"Enviando email de bienvenida a {usuario.email}...")

usuario = Usuario("Ana", "ana@empresa.com")
ValidadorUsuario().validar(usuario)
RepositorioUsuario().guardar(usuario)
ServicioEmail().enviar_email_bienvenida(usuario)