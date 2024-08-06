import { Box, TextField, Divider, IconButton, Button } from '@mui/material'
import { useState } from 'react'
import {useFormContext} from 'react-hook-form'
import AddIcon from '@mui/icons-material/Add';
import { Delete } from '@mui/icons-material';

const JsoninputComponent = ({fields}) => {
    const {register} = useFormContext()
    const [keyValuePairs, setKeyValuePairs] = useState([{key: '', value: ''}])
    const handleKeyValueRemove = (index) => {
        const newPairs = keyValuePairs.filter((_, i) => i !== index);
        setKeyValuePairs(newPairs);
    }

    const handleKeyValuePairAdd = () => {
        setKeyValuePairs([...keyValuePairs, {key: '', value: ''}]);
    }

    return (
        <Box mb={2}>
            <label>{fields.label.toUpperCase()}</label>
            <Divider sx={{marginTop:'10px', marginBottom:'15px'}} />
            {
                keyValuePairs.map((pair, index) => (
                    <Box key={index} display={'flex'} alignItems={'center'} mb={2}>
                        <TextField 
                        fullWidth
                        margin='normal'
                        key={fields.name}
                        label="Key"
                        defaultValue={pair.key}
                        {...register(`${fields.name}[${index}].key`)}
                        placeholder='Key'
                        sx={{marginRight:'5px'}}
                        />
                        <TextField 
                        fullWidth
                        margin='normal'
                        key={fields.name}
                        label="Value"
                        defaultValue={pair.value}
                        {...register(`${fields.name}[${index}].value`)}
                        placeholder='Value'
                        />
                        <IconButton onClick={() => handleKeyValueRemove(index)} variant={"outlined"} color={"secondary"}>
                            <Delete />
                        </IconButton>
                    </Box>
                ))
            }
            <Button variant='contained' color={'primary'} onClick={() => handleKeyValuePairAdd()}><AddIcon /></Button>
            <Divider sx={{marginTop:'10px', marginBottom:'10px'}} />
        </Box>
    )
}

export default JsoninputComponent