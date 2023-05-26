var mix = {
	methods: {
		submitPayment() {
			console.log('qweqwewqeqweqw')
			const orderId = location.pathname.startsWith('/payment/')
				? Number(location.pathname.replace('/payment/', '').replace('/', ''))
				: null
			this.postData(`/api/payment/${orderId}`, {
				name: this.name,
				number: this.number,
				year: this.year,
				month: this.month,
				code: this.code
			})
				.then(() => {
					alert('Успешная оплата')
					this.number = ''
					this.name = ''
					this.year = ''
					this.month = ''
					this.code = ''
					location.assign('/')
				})
				.catch(() => {
					console.warn('Ошибка при оплате')
				})
		}
	},
	data() {
		return {
			number: '',
			month: '',
			year: '',
			name: '',
			code: ''
		}
	}
}