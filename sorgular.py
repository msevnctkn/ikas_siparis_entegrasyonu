ORDER_QUERY = """query ListOrder($pagination: PaginationInput!) {
  listOrder(pagination: $pagination) {
    limit
    hasNext
    page
    count
    data {
      createdAt
      orderedAt
      customer {
        fullName
      }
      orderNumber
      note
      itemCount
      orderLineItems {
        variant {
          barcodeList
          name
          variantValues {
            order
        }
 
        }
        finalPrice
        price
        status
        options {
          name
          productOptionId
          productOptionsSetId
          type
          values {
            applyAfterCampaign
            name
            price
            priceType
            value
          }
        }
    
      }
        attributes {
          orderAttributeId
          orderAttributeOptionId
          value
        
      }
      shippingAddress {
        addressLine1
        addressLine2
         city {
          name
        }
      }
      cancelReason
    
      salesChannel {
        name
      }
    }
  }


   
  listProduct {
    data {
      variants {
        images {
          imageId
          isMain
          isVideo
          order
          fileName
        }
      }
    }
  }

}"""

#





IMAGE_QUERY = """query ProductImages($id: ID!) {
  getProduct(id: $id) {
    id
    name
    media {
      id
      url
      order
    }
  }
}"""


