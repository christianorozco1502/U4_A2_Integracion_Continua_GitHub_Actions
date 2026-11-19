
from flask import Blueprint, jsonify, request
from models import db, Juego

api = Blueprint("api", __name__)


# Obtener todos los videojuegos
@api.route("/juegos", methods=["GET"])
def obtener_juegos():
    juegos = Juego.query.all()
    lista = []

    for juego in juegos:
        lista.append({
            "id": juego.id,
            "nombre": juego.nombre,
            "descripcion": juego.descripcion,
            "precio": float(juego.precio)
        })

    return jsonify(lista), 200


# Agregar un videojuego
@api.route("/juegos", methods=["POST"])
def agregar_juego():
    datos = request.get_json(silent=True)

    if not isinstance(datos, dict):
        return jsonify({"error": "Datos invalidos"}), 400

    if not all(campo in datos for campo in ["nombre", "descripcion", "precio"]):
        return jsonify({"error": "Faltan datos del juego"}), 400

    if not isinstance(datos["nombre"], str) or not isinstance(datos["descripcion"], str):
        return jsonify({"error": "Nombre o descripcion invalidos"}), 400

    nombre = datos["nombre"].strip()
    descripcion = datos["descripcion"].strip()

    try:
        precio = float(datos["precio"])
        if not nombre or not descripcion or not 0 <= precio <= 9999999.99:
            return jsonify({"error": "Datos invalidos"}), 400
    except (ValueError, TypeError, OverflowError):
        return jsonify({"error": "Precio invalido"}), 400

    juego = Juego(
        nombre=nombre,
        descripcion=descripcion,
        precio=precio
    )

    db.session.add(juego)
    db.session.commit()

    return jsonify({
        "mensaje": "Juego agregado correctamente",
        "id": juego.id
    }), 201


# Obtener un videojuego por su ID
@api.route("/juegos/<int:id>", methods=["GET"])
def obtener_juego(id):
    juego = db.session.get(Juego, id)

    if not juego:
        return jsonify({"error": "Juego no encontrado"}), 404

    return jsonify({
        "id": juego.id,
        "nombre": juego.nombre,
        "descripcion": juego.descripcion,
        "precio": float(juego.precio)
    }), 200


# Modificar un videojuego
@api.route("/juegos/<int:id>", methods=["PUT"])
def modificar_juego(id):
    juego = db.session.get(Juego, id)

    if not juego:
        return jsonify({"error": "Juego no encontrado"}), 404

    datos = request.get_json(silent=True)

    if not isinstance(datos, dict):
        return jsonify({"error": "Datos invalidos"}), 400

    if not all(campo in datos for campo in ["nombre", "descripcion", "precio"]):
        return jsonify({"error": "Faltan datos del juego"}), 400

    if not isinstance(datos["nombre"], str) or not isinstance(datos["descripcion"], str):
        return jsonify({"error": "Nombre o descripcion invalidos"}), 400

    nombre = datos["nombre"].strip()
    descripcion = datos["descripcion"].strip()

    try:
        precio = float(datos["precio"])
        if not nombre or not descripcion or not 0 <= precio <= 9999999.99:
            return jsonify({"error": "Datos invalidos"}), 400
    except (ValueError, TypeError, OverflowError):
        return jsonify({"error": "Precio invalido"}), 400

    juego.nombre = nombre
    juego.descripcion = descripcion
    juego.precio = precio

    db.session.commit()

    return jsonify({
        "mensaje": "Juego actualizado correctamente",
        "id": juego.id
    }), 200

# Eliminar un videojuego
@api.route("/juegos/<int:id>", methods=["DELETE"])
def eliminar_juego(id):
    juego = db.session.get(Juego, id)

    if not juego:
        return jsonify({"error": "Juego no encontrado"}), 404

    db.session.delete(juego)
    db.session.commit()

    return "", 204