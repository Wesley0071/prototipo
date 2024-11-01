def configuracao(aplicativo):
    aplicativo.secret_key = 'chavedeseguranca'# os formulario so renderizam se esta chave estiver configurada 
    aplicativo.config['UPLOAD_FOLDER'] = 'uploads'# configuraçao do caminho para o uploads de arquivos

    # Configurações do banco de dados
    aplicativo.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
    aplicativo.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False