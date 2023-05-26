var mix = {
	methods: {
		signUp () {
			const username = document.querySelector('#login').value
			const password = document.querySelector('#password').value
			this.postData('/api/sign-up/', JSON.stringify({ name, username, password }))
				.then(({ data, status }) => {
					location.assign(`/`)
				})
		}
	},
	mounted() {
	},
	data() {
		return {}
	}
}