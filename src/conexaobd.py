import psycopg2

hostname = 'localhost'  
username = 'bruno'
password = 'bruno'
database = 'ProjetoPython'

try:
    # Conectar ao banco de dados
    conn = psycopg2.connect(
        host=hostname,
        user=username,
        password=password,
        database=database,
        client_encoding='utf-8'
    )

    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO temas (data, tema)
        VALUES (%s, %s);
    """, (data, tema))

    conn.commit()
    print("Dados inseridos com sucesso!")

    cursor.execute("SELECT * FROM temas;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print("Erro ao inserir dados no banco de dados:", e)
