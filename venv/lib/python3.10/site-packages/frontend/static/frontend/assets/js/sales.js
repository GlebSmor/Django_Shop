var mix = {
    methods: {
        getSales(page = 1) {
            this.getData("/api/sales/", {
                currentPage: page,
            }).then(data => {
                this.salesCards = data.items
                this.currentPage = data.currentPage
                this.lastPage = data.lastPage
            })
        },
    },
    mounted() {
        this.getSales();
    },
    data() {
        return {
            salesCards: [],
            currentPage: 1,
            lastPage: 1,
            // TODO добавить пагинацию
        }
    },
}