from rembg import new_session, remove
input_path = '06列表/original.jpg'
output_path = '06列表/result.png'
session = new_session("u2net")
with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        Input = i.read()
        Output = remove(Input, session=session)
        o.write(Output)
