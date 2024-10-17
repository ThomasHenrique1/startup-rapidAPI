document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('startup-form');
    const input = document.getElementById('startup-input');
    const responseDiv = document.getElementById('response');
    const responseArticle = document.getElementById('api-response'); // Alterado para selecionar o <article>

    // Função para formatar texto em Markdown para HTML
    function formatMarkdown(text) {
        return text
            .replace(/## (.*?)/g, '<h2>$1</h2>')  // Converte ## para <h2>
            .replace(/(?<!\*)\*\*(.+?)\*\*(?!\*)/g, '<strong>$1</strong>')  // Converte **texto** para <strong> se não estiver em negrito já
            .replace(/# (.*?)/g, '<h1>$1</h1>')  // Converte # para <h1>
            .replace(/\n/g, '<br>');  // Converte novas linhas para <br>
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault(); // Previne o envio padrão do formulário

        const userInput = input.value;

        // Envia a solicitação para o Flask
        const res = await fetch('/generate-startup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ input: userInput })
        });

        const data = await res.json();

        // Exibe a resposta da API com formatação
        if (data.error) {
            responseArticle.innerHTML = `Erro: ${data.error}`; // Atualizado para usar <article>
        } else {
            responseArticle.innerHTML = formatMarkdown(data.msg); // Aplica a formatação ao texto
        }

        // Limpa o campo de entrada após enviar
        input.value = '';
    });
});
