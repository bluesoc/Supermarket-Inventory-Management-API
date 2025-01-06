// Vue.js
const { createApp } = Vue;

// Control #app
createApp({
    // Root component (object)
    data() {
        return {
            index: 1,
            index1: true,
            index2: false,
            index3: false,
            showChart: false,
            jsonData: {
                labels: [],
                data: []
            },
        }
    },
    // Configure custom delimiters
    delimiters: ['[[', ']]'],
    methods: {
        updateApp(val) {
            this.index1 = false;
            this.index2 = false;
            this.index3 = false;
            this.index4 = false;

            // Switch case for NavBar
            switch (val) {
                case 1:
                    this.index1 = true;
                    break;
                case 2:
                    this.index2 = true;
                    break;
                case 3:
                    this.index3 = true;
                    break;
                case 4:
                    this.index4 = true;
                    break;
                default:
                    console.warn('Invalid', val);
            }
            // Update current index
            this.index = val;
        },
        toggleChart() {
            this.showChart = !this.showChart;
            // Reload Chart
            if (this.showChart) {
                this.fetchData();
            }
        },
        fetchData() {
            fetch(viewURL)
                .then(response => response.json())
                .then(data => {
                    this.jsonData.labels = [];
                    this.jsonData.data = [];

                    data.forEach(item => {
                        // Check if item already exists
                        let index = this.jsonData.labels.indexOf(item.fields.category);

                        if (index >= 0) {
                            this.jsonData.data[index] += item.fields.quantity;
                        } else {
                            this.jsonData.labels.push(item.fields.category);
                            this.jsonData.data.push(item.fields.quantity);
                        }
                    });
                    this.renderChart(); // Render Chart
                })
                .catch(error => console.error('Erro:', error));
        },
        renderChart() {
            const ctx = document.getElementById('myChart').getContext('2d');
            // Clear old chart
            if (this.myChart) {
                this.myChart.destroy();
            }
            this.myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: this.jsonData.labels,
                    datasets: [{
                        label: 'Stock',
                        data: this.jsonData.data,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(153, 102, 255, 0.2)'
                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        },
        loadJson() {
            fetch(viewURL)
                    .then(response => response.json())
                    .then(data => {
                        // Well...
                        this.jsonData = data;
                    })
                    .catch(error => console.error('Error:', error));    
        },
    },
    mounted() {
        this.fetchData();
    }
}).mount('#app');