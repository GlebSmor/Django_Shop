var mix = {
	methods: {
		getOrder(orderId) {
			if(typeof orderId !== 'number') return
			this.getData(`/api/order/${orderId}/`)
				.then(data => {
					this.orderId = data.id
					this.createdAt = data.createdAt
					this.fullName = data.fullName
					this.phone = data.phone
					this.email = data.email
					this.deliveryType = data.deliveryType
					this.city = data.city
					this.address = data.address
					this.paymentType = data.paymentType
					this.status = data.status
					this.totalCost = data.totalCost
					this.products = data.products
					console.log(this.products)
					if (typeof data.paymentError !== 'undefined') {
						this.paymentError = data.paymentError
					}
				})
		},
		confirmOrder() {
			if (this.orderId !== null) {
				this.postData(`/api/order/${this.orderId}/`, { ...this })
					.then(({ data: { orderId } }) => {
						alert('Заказ подтвержден')
						location.replace(`/payment/${orderId}/`)
					})
					.catch(() => {
						console.warn('Ошибка при подтверждения заказа')
					})
			}
		},
		auth() {
			const username = document.querySelector('#username').value
			const password = document.querySelector('#password').value
			this.postData('/api/sign-in/', JSON.stringify({ username, password }))
				.then(({ data, status }) => {
					location.assign(`/orders/${this.orderId}`)
				})
				.catch(() => {
					alert('Ошибка авторизации')
				})
		}
	},
	mounted() {
		if(location.pathname.startsWith('/orders/')) {
			const orderId = location.pathname.replace('/orders/', '').replace('/', '')
			this.orderId = orderId.length ? Number(orderId) : null
			this.getOrder(this.orderId);
		}
	},
	data() {
		return {
			orderId: null,
			createdAt: null,
			fullName: null,
			phone: null,
			email: null,
			deliveryType: null,
			city: null,
			address: null,
			paymentType: null,
			status: null,
			totalCost: null,
			products: [],
			paymentError: null,
		}
	},
}