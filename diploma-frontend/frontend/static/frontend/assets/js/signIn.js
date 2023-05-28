var mix = {
	methods: {
		signIn () {
			const username = document.querySelector('#login').value
			const password = document.querySelector('#password').value
			this.postData('/api/sign-in/', JSON.stringify({ username, password }))
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