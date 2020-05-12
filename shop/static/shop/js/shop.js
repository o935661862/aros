var a = new Vue({
	el: '#starting',
	delimiters: ['${', '}'],
	data: {
		shops: [],
		users: [],
		currentShop: {},
		selectedUser: {},
		message: null,
		newShop: { 'name': null, 'owner': null },
		},
	mounted: function() {
	this.getShops();
	},
	methods: {
	
		getShops: function() {
			this.$http.get('/api/shop')
					.then((response) => {
					this.shops = response.data;
					// console.log(response.data);
					})
					.catch((err) => {
					console.log(err);
					})
		},
		
		getUsers: function() {
			this.$http.get('/user/')
					.then((response) => {
					this.users = response.data;
					// console.log(response.data);
					})
					.catch((err) => {
					console.log(err);
					})
		},
		
		getShop: function(id) {
			this.$http.get('/api/shop/' + id)
					.then((response) => {
					this.currentShop = response.data;
					console.log(typeof(this.currentShop.owner.id));
					this.getUsers();
					})
					.then(() =>{$("#editShopModal").modal('show');})
					.catch((err) => {
					console.log(err);
					})
		},
		
		addShop: function() {
			console.log(this.newShop);
			this.$http.post('/api/shop/', this.newShop, {headers: {'X-CSRFToken':csrftoken }})
					.then((response) => {
					$("#addShopModal").modal('hide');
					this.getShops();
					})
					.catch((err) => {
					console.log(err);
					})
		},
		
		updateShop: function() {
			console.log(this.currentShop);
			this.$http.put('/api/shop/' + this.currentShop.id + '/',	this.currentShop, {headers: {'X-CSRFToken':csrftoken }})
					.then((response) => {
					
					this.currentShop = response.data;
					this.getShops();
					})
					.catch((err) => {
					console.log(err);
					})
		},
		
		deleteShop: function(id) {
			this.$http.delete('/api/shop/' + id + '/', {headers: {'X-CSRFToken':csrftoken }} )
					.then((response) => {
					this.getShops();
					})
					.catch((err) => {
					console.log(err);
				})
			},
	},

});