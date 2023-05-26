var mix = {
	methods: {
		signUp () {
			const name = document.querySelector('#name').value
			const username = document.querySelector('#login').value
			const password = document.querySelector('#password').value
			this.postData('/api/sign-up', JSON.stringify({ name, username, password }))
				.then(({ data, status }) => {
					location.assign(`/`)
				})
				.catch(() => {
					alert('Ошибка авторизации!')
				})
		}
	},
	mounted() {
	},
	data() {
		return {}
	}
}