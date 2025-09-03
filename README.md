# MiTMGPT - ChatGPT Local Vulnerable App con HTTPS

Esta es una aplicación Flask vulnerable a MITM, con certificados autofirmados para demostrar interceptación incluso en tráfico HTTPS (cuando no se valida el certificado correctamente).

## Características

- Certificados autofirmados para HTTPS
- Cookies inseguras
- Transmisión de mensajes y credenciales, ahora en HTTPS
- Permite simular ataques MITM con falsos certificados

## Instalación

```bash
git clone https://github.com/tuusuario/MiTMGPT.git
cd MiTMGPT
pip install -r requirements.txt
python MiTMGPT.py
```

Abre tu navegador en `https://localhost:5000`

> ⚠️ Acepta el certificado autofirmado para continuar.

## Credenciales

- Usuario: `admin`
- Contraseña: `1234`

## Advertencia

Esta app es para educación y pruebas en entornos controlados.
