async function deleteFilme(filmeId) {
    const response = await fetch(`/delete_filme/${filmeId}`, {
        method: 'DELETE'
    });

    if (response.ok) {
        const data = await response.json();
        if (data.redirect && data.redirect.url) {
            window.location.href = data.redirect.url;
        } else {
            alert('Filme deletado com sucesso!');
        }
    } else {
        const errorData = await response.json();
        alert(`Erro ao deletar filme: ${errorData.detail}`);
    }
}