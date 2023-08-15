<script type="application/ld+json">
{
  "@context": "http://schema.org/",
  "@graph": [
    {
      "@type": "Product",
      "name": "Zippy's Spiritual Reading (One Topic)",
      "image": ["10001.png"],
      "description": "20 mins only in $35. Get a spiritual reading with one topic of your choice.",
      "offers": {
        "@type": "Offer",
        "price": "35.00",
        "priceCurrency": "USD",
        "availability": "http://schema.org/InStock"
      }
    },
    {
      "@type": "Product",
      "name": "Zippy's Spiritual Reading (Two Topics)",
      "image": ["10001.png"],
      "description": "40 mins only in $50. Get a spiritual reading with two topics of your choice.",
      "offers": {
        "@type": "Offer",
        "price": "50.00",
        "priceCurrency": "USD",
        "availability": "http://schema.org/InStock"
      }
    },
    {
      "@type": "Product",
      "name": "Zippy's Spiritual Reading (Three Topics)",
      "image": ["10001.png"],
      "description": "1 hour only in $70. Get a spiritual reading with three topics of your choice.",
      "offers": {
        "@type": "Offer",
        "price": "70.00",
        "priceCurrency": "USD",
        "availability": "http://schema.org/InStock"
      }
    }
  ]
}
</script>


// Simulating dynamic product grid generation
const productGrid = document.querySelector('.product-grid');

// Sample product data
const products = [
  { name: 'Product 1', type: 'Type 1' },
  { name: 'Product 2', type: 'Type 2' },
  { name: 'Product 3', type: 'Type 1' },
  // Add more product items here...
];

// Function to generate product grid items
function generateProductGrid(products) {
  productGrid.innerHTML = '';
  
  products.forEach(product => {
    const productItem = document.createElement('div');
    productItem.classList.add('product');
    productItem.innerHTML = `
      <h3>${product.name}</h3>
      <p>Type: ${product.type}</p>
    `;
    
    productGrid.appendChild(productItem);
  });
}

// Initial generation of product grid
generateProductGrid(products);

// Add click event listeners for product types
const productTypes = document.querySelectorAll('.product-type');
productTypes.forEach(type => {
  type.addEventListener('click', () => {
    // Fetch products based on selected type and generate grid
    const selectedType = type.textContent;
    const filteredProducts = products.filter(product => product.type === selectedType);
    generateProductGrid(filteredProducts);
  });
});

// Add click event listeners for pagination
const pageNumbers = document.querySelectorAll('.page-number');
pageNumbers.forEach(number => {
  number.addEventListener('click', () => {
    // Fetch products for selected page number and generate grid
    const selectedPage = number.textContent;
    // Perform pagination logic here...
    // Fetch products based on selected page and generate grid
    // ...
  });
});
