# TESTE CAES

---

## TELA DE CADASTRO

### Cenário: Cadastrar usuário com sucesso

1. Adicionar um nome
2. Adicionar email válido
3. Adicionar um telefone
4. Adicionar data de nascimento
5. Adicionar uma senha
6. Repetir a mesma senha anterior
7. Aceitar os termos de privacidade
8. Clicar em Registrar-se

**Resultado Esperado:** Cadastrar o usuário e acessar o banco de questões

### Cenário: Se cadastrar sem preencher um dos campos pedidos

1. Deixar um campo em branco
2. Clicar em Registrar-se

**Resultado Esperado:** Mensagem informando que todos os campos devem ser preenchidos

### Cenário: Se cadastrar com um email inválido

1. Adicionar um email inválido
2. Clicar em Registrar-se

**Resultado Esperado:** Mensagem de erro informando que o email é inválido

### Cenário: Se cadastrar repetindo um email já cadastrado

1. Adicionar um email que já possui cadastro
2. Clicar em Registrar-se

**Resultado Esperado:** Mensagem informando que o email/usuário já está cadastrado

### Cenário: Se cadastrar usando uma data de nascimento que ainda não chegou

1. Adicionar uma data de nascimento que ainda não chegou (ex: 05/09/2025)
2. Clicar em Registrar-se

**Resultado Esperado:** Mensagem informando que a data de nascimento está inválida

### Cenário: Não cadastrar uma senha de acesso

1. Não colocar senha
2. Clicar em Registrar-se

**Resultado Esperado:** Mensagem informando que é obrigatório cadastrar uma senha

### Cenário: Confirmar uma senha com caracteres diferentes da senha cadastrada

1. Confirmar a senha com caracteres errados
2. Clicar em Registrar-se

**Resultado Esperado:** Mensagem informando que a confirmação da senha está inválida

### Cenário: Não confirmar a senha cadastrada

1. Não repetir a senha cadastrada
2. Clicar em Registrar-se

**Resultado Esperado:** Mensagem informando que é obrigatório confirmar a senha cadastrada

### Cenário: Se cadastrar sem confirmar que concorda com os Termos e Políticas de privacidade

1. Não clicar na caixa de concordar com os Termos e Políticas de privacidade
2. Clicar em Registrar-se

**Resultado Esperado:** Mensagem informando que é obrigatório concordar com os Termos e Políticas de privacidade

---

## PLANO PREMIUM

### Cenário: Clicar em ser premium e ver os planos premium

1. Clique no botão “Seja premium”

**Resultado Esperado:** Ter acesso a todos os planos premium

---

## TELA DE LOGIN

### Cenário: Logar com sucesso

1. Adicionar email já cadastrado
2. Adicionar senha já cadastrada
3. Clicar no botão “Acessar”

**Resultado Esperado:** Acessar o banco de questões com sucesso

### Cenário: Criar uma conta

1. Clicar no botão “Criar nova conta”

**Resultado Esperado:** Acessar a página para cadastrar uma conta

### Cenário: Receber email para recuperar senhas

1. Clicar em “Esqueceu a senha?”
2. Adicionar um email cadastrado
3. Clicar no botão “Recuperar”

**Resultado Esperado:** Mensagem informando que foi enviado o link de recuperação de senha para o email

### Cenário: Adicionar um email inválido na recuperação de senha

1. Clicar em “Esqueceu a senha?”
2. Adicionar um email não cadastrado
3. Clicar no botão “Recuperar”

**Resultado Esperado:** Mensagem informando que o email não está cadastrado no banco de questões

---

## FILTRO DE QUESTÕES

### Cenário: Fazer um filtro utilizando todos os campos disponíveis

1. Colocar uma palavra-chave
2. Selecionar a Disciplina
3. Selecionar o Assunto
4. Selecionar a Carreira
5. Selecionar o Cargo
6. Selecionar o Órgão
7. Selecionar a Banca
8. Selecionar a opção de “Canceladas”
9. Selecionar a opção de “Desatualizadas”
10. Selecionar a opção de “Tipos de questões”
11. Clicar no botão “Filtrar questões”

**Resultado Esperado:** Aparecem todas as questões do banco de dados que correspondem ao filtro

### Cenário: Filtrar questão apenas por palavra-chave

1. Adicionar uma palavra-chave no campo “Faça uma busca por palavra-chave”
2. Deixar todos os outros campos em branco
3. Selecionar a opção de “Canceladas”
4. Selecionar a opção de “Desatualizadas”
5. Selecionar a opção de “Tipos de questões”
6. Clicar no botão “Filtrar questões”

**Resultado Esperado:** Aparecem todas as questões do banco de dados relacionadas à palavra-chave

---

## DASHBOARD

### Cenário: Analisar o desempenho total do estudante a partir de uma data inicial e final

1. Selecionar a Data Inicial
2. Selecionar a Data Final

**Resultado Esperado:** Ver o total de questões respondidas, total de respostas corretas, total de respostas erradas, taxa de acerto e total de questões comentadas

### Cenário: Zerar o percentual de rendimentos

1. Acessar a página “Dashboard”
2. Clicar em “Zerar estatística”

**Resultado Esperado:** Mensagem informando que a estatística foi zerada e o gráfico ficará cinza

---

## PERFIL

### Cenário: Adicionar uma foto com sucesso

1. Clicar no ícone de edição “user imagem”
2. Selecionar uma imagem

**Resultado Esperado:** Imagem deve ser carregada e adicionada com sucesso

### Cenário: Erro por deixar um campo vazio ao adicionar Dados Pessoais, Endereço e Contato

1. Deixar um dos campos vazio
2. Clicar em “Salvar”

**Resultado Esperado:** Mensagem informando que todos os campos devem ser preenchidos
