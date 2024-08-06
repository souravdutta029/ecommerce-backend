import { useState, useEffect } from 'react'
import useApi  from '../../hooks/APIHandler'
import { useNavigate } from 'react-router-dom'
import { Box, Breadcrumbs, IconButton, TextField, Typography } from '@mui/material'
import { DataGrid, GridToolbar } from '@mui/x-data-grid'
import { isValidUrl } from '../../utils/Helper'
import LinearProgress from '@mui/material/LinearProgress'
import Add from '@mui/icons-material/Add'
import Delete from '@mui/icons-material/Delete'
import Edit from '@mui/icons-material/Edit'
import ExpandLessRounded from '@mui/icons-material/ExpandLessRounded'
import ExpandMoreRounded from '@mui/icons-material/ExpandMoreRounded'
import ExpandableRow from './ExpandableRow'

const ManageCategories = () => {
    const [data, setData] = useState([])
    const [columns, setColumns] = useState([])
    const [paginationModel, setPaginationModel] = useState({
        page:0,
        pageSize:5
    })

    const [totalItems, setTotalItems] = useState(0)
    const [searchQuery, setSearchQuery] = useState('')
    const [debounceSearch, setDebounceSearch] = useState('')
    const [ordering, setOrdering] = useState([{field:'id', sort:'desc'}])
    const {error, loading, callApi} = useApi()
    const navigate = useNavigate()

    useEffect(() => {
        const timer = setTimeout(() => {
            setDebounceSearch(searchQuery)
        }, 1000)

        return () => {clearTimeout(timer)}

    }, [searchQuery])

    const getCategories = async () => {
        let order = '-id'
        if (ordering.length > 0) {
            order = ordering[0].sort === 'asc'?ordering[0].field:'-'+ordering[0].field
        }
        const result = await callApi({
            url: 'products/categories/',
            method: 'GET',
            params: {
                page: paginationModel.page+1,
                pageSize: paginationModel.pageSize,
                search: debounceSearch,
                ordering: order
            }
        })

        if (result) {
            setData(result.data.data.data)
            setTotalItems(result.data.data.totalItems)
            generateColumns(result.data.data.data)
        }
    }

    const onAddClick = (params) => {
        console.log(params)
        navigate('/form/category')
    }

    const onAEditClick = (params) => {
        console.log(params)
    }

    const onDeleteClick = (params) => {
        console.log(params)
    }

    const generateColumns = (data) => {
        if(data.length > 0) {
            const columns = [{
                field: 'action', 
                headerName: 'Action',
                width: 180,
                sortable: false,
                renderCell: (params) => {
                    return <>
                        <IconButton onClick={() => onAddClick(params)}>
                            <Add color='light' />
                        </IconButton>

                        <IconButton onClick={() => onAEditClick(params)}>
                            <Edit color='primary' />
                        </IconButton>

                        <IconButton onClick={() => onDeleteClick(params)}>
                            <Delete color='secondary' />
                        </IconButton>
                    </>
                }
            }, {
                field: 'expand',
                headerName: 'Expand',
                width: 100,
                sortable: false,
                renderCell: (params) => {
                    return <IconButton onClick={() => {
                        const updatedRows = data.map((row) => {
                            if (row.id === params.row.id) {
                                return {...row, open: !row.open}
                            }
                            return row
                        })
                        setData([...updatedRows])
                    }}>
                        {params.row?.open?<ExpandLessRounded/>:<ExpandMoreRounded/>}
                    </IconButton>
                }
            }];
            for(const key in data[0]) {
                if (key === 'children') {
                    columns.push({
                        field: key, 
                        headerName: key.charAt(0).toUpperCase()+key.slice(1).replaceAll('_', ' '),
                        width: 150,
                        sortable: false,
                        renderCell: (params) => {
                            return <Typography variant="body2" pt={3} pb={3}>{params.row.children?.length}</Typography>
                                
                        }
                    })
                                
                } else if (key === 'image') {
                    columns.push({
                        field: key, 
                        headerName: key.charAt(0).toUpperCase()+key.slice(1).replaceAll('_', ' '),
                        width: 150,
                        sortable: false,
                        renderCell: (params) => {
                            return (params.row.image && params.row.image !== "" && isValidUrl(params.row.image))?
                                <img src={params.row.image} alt={params.row.name} style={{width:70, height:70, padding:5}} />:
                                <Typography variant="body2" pt={3} pb={3}>No Image</Typography>
                        }
                    })
                } else {
                    columns.push({
                        field: key, 
                        headerName: key.charAt(0).toUpperCase()+key.slice(1).replaceAll('_', ' '),
                        width: 150
                    })
                }
            }
            setColumns(columns)
        }
    }

    const handleSorting = (newModel) => {
        setOrdering(newModel)
    }

    useEffect(() => {
        getCategories()
    }, [paginationModel, debounceSearch, ordering])

    return (
        <Box component={'div'} sx={{width:'100%'}}>
            <Breadcrumbs>
                <Typography variant='body2' onClick={() => navigate('/')}>Home</Typography>
                <Typography variant='body2' onClick={() => navigate('/manage/category')}>Manage Categories</Typography>
            </Breadcrumbs>
            <TextField label="Search" variant='outlined' fullWidth onChange={(e) => setSearchQuery(e.target.value)} margin='normal' />
            <DataGrid 
            rows={data} 
            columns={columns} 
            rowHeight={75}
            sortingOrder={['asc', 'desc']}
            sortModel={ordering}
            onSortModelChange={handleSorting}
            paginationMode='server'
            initialState={{
                ...data.initialState,
                pagination: {paginationModel:paginationModel}
            }}
            pageSizeOptions={[5, 10, 20, 25, 30]}
            pagination
            rowCount={totalItems}
            loading={loading}
            rowSelection={false}
            onPaginationModelChange={(pageDetails) => {
                setPaginationModel({
                    page:pageDetails.page,
                    pageSize:pageDetails.pageSize
                })
            }}
            slots={
                {
                    loadingOverlay: LinearProgress,
                    toolbar: GridToolbar,
                    row: (props) => {
                        return <ExpandableRow row={props.row} props={props} onAEditClick={onAEditClick} onDeleteClick={onDeleteClick}/>
                    }
                }
            }
            />
        </Box>
    )
}

export default ManageCategories