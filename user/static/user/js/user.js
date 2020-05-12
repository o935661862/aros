Vue.component('table-vue',
{
	delimiters: ["((","))"],
	props: ['users', 'userkeys'],
	template: 
		`
		<table class = 'table'>
			<thead>
				<tr>
					<th scope="col" v-for = 'userkey in userkeys'>(( userkey ))</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for = 'user in users'>
					<td v-for = 'userkey in userkeys'>((user[userkey]))</td>
				</tr>
			</tbody>
		</table>
		`
}
)










app = new Vue({
	delimiters: ["((","))"],
	el: '#tableDiv',
	data: {
		users: [{'id': 1,'username':'user1'}, {'id': 2,'username':'user2'}, {'id': 3,'username':'user3'}, {'id': 4,'username':'user4'},],
	},
	computed: {
		userkeys: function(){
			return Object.keys(this.users[0])
		}
	},
});