ORDER_QUERY = """query ListOrder($pagination: PaginationInput) {
  listOrder(pagination: $pagination) {
    limit
    hasNext
    page
    count
    data {
      createdAt
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
        status
      }
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


