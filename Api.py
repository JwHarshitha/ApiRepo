from flask import Flask, jsonify, request

app = Flask(__name__)

items_list=[
    {'id': 1, 'name': 'Antique Wall Clock', 'artist': 'George Orwell'},
    {'id': 2, 'name': 'Van gogh Painting', 'artist': 'Van Gogh'},
    {'id': 3, 'name': 'The Great Gatsby item', 'artist': 'F. Scott Fitzgerald'},
    {'id': 4, 'name': 'Peonies Painting', 'artist': 'Harper Lee'},
    {'id': 5, 'name': 'Table lamp', 'artist': 'Harper Lee'}
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items_list)

@app.route('/items/getting_item/<int:id>', methods=['GET'])
def get_item_id(id):
    item=next((item for item in items if item['id']==id), None)
    if item:
        return jsonify(item)
    return jsonify({'message':'Item not found'}), 404

@app.route('/items/<int:id>',methods=['POST'])
def add_item():
    new_item={
        'id':items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'artist': request.json['artsit']
    }
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = next((item for item in items if item['id'] == id), None)
    if item:
        item['name'] = request.json.get('name', item['name'])
        item['artist'] = request.json.get('artist', item['artist'])
        return jsonify(item)
    return jsonify({'message': 'item not found'}), 404

@app.route('/items/<int:id>',methods=['DELETE'])
def delete_item(id):
    global items
    items = [item for item in items if item['id'] != id]
    return jsonify({'message': 'item deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)