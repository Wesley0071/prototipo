<?php
header('Content-Type: application/json');

// Configurações de conexão com o banco de dados
$servername = "localhost"; // Endereço do servidor (pode ser um IP ou um domínio)
$username = "root";  // Nome de usuário do banco de dados
$password = "";     // Senha do banco de dados
$dbname = "lint";       // Nome do banco de dados

// Criando a conexão
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexão
if ($conn->connect_error) {
    die(json_encode(['error' => 'Conexão falhou: ' . $conn->connect_error]));
}

// Rota para obter usuários
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $result = $conn->query("SELECT * FROM alunos");
    $users = $result->fetch_all(MYSQLI_ASSOC);
    echo json_encode($users);
}

// Rota para adicionar um usuário
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    $nome = $data['nome'];
    $email = $data['email'];
    $telefone = $data['telefone'];
    $conn->query("INSERT INTO alunos (nome, email, telefone) VALUES ('$nome', '$email', '$telefone')");
    echo json_encode(['status' => 'Usuário adicionado']);
}

// Rota para atualizar um usuário
if ($_SERVER['REQUEST_METHOD'] === 'PUT') {
    $data = json_decode(file_get_contents('php://input'), true);
    $id = $data['id'];
    $nome = $data['nome'];
    $email = $data['email'];
    $telefone = $data['telefone'];
    $conn->query("UPDATE alunos SET nome='$nome', email='$email', telefone='$telefone' WHERE id=$id");
    echo json_encode(['status' => 'Usuário atualizado']);
}

// Rota para deletar um usuário
if ($_SERVER['REQUEST_METHOD'] === 'DELETE') {
    $data = json_decode(file_get_contents('php://input'), true);
    $id = $data['id'];
    $conn->query("DELETE FROM alunos WHERE id=$id");
    echo json_encode(['status' => 'Usuário deletado']);
}

// Fechar conexão
$conn->close();
