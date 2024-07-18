# Exercícios de revisão de funções

Siga a ordem e implemente um método após o outro.
Organize seu projeto para que o código seja reutilizado o máximo possível.
Acrescente comentários e informe os tipos dos parâmetros e retornos.

Crie um método que recebe um número que representa uma idade, e retorna:

- True, se houver maioridade (>= 18 anos, crie uma CONSTANTE para o ‘18’)
- False, do contrário

Crie um método que recebe uma string contendo um e-mail e retorna:

- True, se for um e-mail válido. Para ser válido, precisa:
    - iniciar com letras, números ou ‘_’
    - seguido de um ‘@’
    - seguido de combinação de letras, números ou ‘_’
    - seguido de ‘.com’ (vamos ignorar outros e-mails)
- False, do contrário

Crie um método que solicita ao usuário um nome completo válido. Enquanto o nome não for válido, siga solicitando.
Retorne:

- O nome, caso tenha pelo menos duas palavras. ‘Capitalize’ a string retornada
- None, caso o usuário não informe valor nenhum e aperte ‘enter’

## Sistema de cadastro de alunos de pré-escola

Utilize os métodos acima para completar o desenvolvimento. Você está criando um sistema que valida as informações de
responsáveis e alunos que estão sendo matriculados em uma pré-escola.

Inicie a aplicação solicitando os dados do responsável, sendo:

- nome do responsável
- ano de nascimento
- e-mail
  Apenas avance quando todas as informações forem válidas. Se o usuário apertar ‘enter’ (sem digitar nada) em qualquer
  um
  dos campos abandone o cadastro por completo.

Solicite as informações de um contato auxiliar. Siga o mesmo fluxo dos dados do responsável, porém não abandone o
cadastro caso as informações não forem fornecidas (contato auxiliar é opcional).

Solicite as informações do aluno. Siga o mesmo fluxo de cadastro do responsável (cadastro obrigatório), porém não pode
haver maioridade.

