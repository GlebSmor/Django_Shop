var mix = {
	methods: {
		getHistoryOrder() {
			this.getData("/api/orders")
				.then(data => {
					console.log(data)
					this.orders = data
				}).catch(() => {
				this.orders = []
				console.warn('Ошибка при получении списка заказов')
			})
		}
	},
	mounted() {
		this.getHistoryOrder();
	},
	data() {
		return {
			orders: [],
		}
	}
}